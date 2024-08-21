import tkinter as tk
from pprint import pprint
from tkinter import ttk, filedialog, messagebox
import subprocess
import os
import json
import threading
import time

import argparse
import os
import shutil
import sys
from os.path import isfile, join

from google.protobuf.text_format import ParseBool

from run_chat_dev import run_chat_dev


class CodeGeneratorUI:
    def __init__(self, root, args):
        self.root = root
        self.root.title("Code Generator and Evaluator")

        self.model_types = ["GPT_3_5_TURBO", "GPT_4", "GPT_4_32K", "GPT_4_TURBO"]
        self.project_files = self.load_project_files()

        self.running = False
        self.thread = None

        self.args = args
        self.dry_run = tk.BooleanVar(value=ParseBool(args.dry_run))
        self.one_shot = tk.BooleanVar(value=False)
        self.create_widgets()

    def load_project_files(self):
        project_files_dir = "Requirements"
        return [f for f in os.listdir(project_files_dir) if os.path.isfile(os.path.join(project_files_dir, f))]

    def create_widgets(self):
        # Dry run checkbox
        self.dry_run_checkbox = tk.Checkbutton(self.root, text="Dry Run", variable=self.dry_run)
        self.dry_run_checkbox.grid(row=3, column=0, padx=10, pady=10)
        self.one_shot_checkbox = tk.Checkbutton(self.root, text="One Shot", variable=self.one_shot)
        self.one_shot_checkbox.grid(row=3, column=1, padx=10, pady=10)

        # Model type selection with checkboxes
        self.model_label = tk.Label(self.root, text="Model Types:")
        self.model_label.grid(row=0, column=0, padx=10, pady=10)
        self.model_vars = {model: tk.BooleanVar() for model in self.model_types}
        for i, model in enumerate(self.model_types):
            chk = tk.Checkbutton(self.root, text=model, variable=self.model_vars[model])
            chk.grid(row=0, column=i+1, padx=5, pady=10)

        # Project file selection with checkboxes
        self.project_label = tk.Label(self.root, text="Project Files:")
        self.project_label.grid(row=1, column=0, padx=10, pady=10)
        self.project_vars = {project: tk.BooleanVar() for project in self.project_files}
        for i, project in enumerate(self.project_files):
            chk = tk.Checkbutton(self.root, text=project, variable=self.project_vars[project])
            chk.grid(row=1, column=i+1, padx=5, pady=10)

        # Start/Stop buttons
        self.start_button = tk.Button(self.root, text="Start Generation", command=self.start_generation)
        self.start_button.grid(row=2, column=0, padx=10, pady=10)
        self.stop_button = tk.Button(self.root, text="Stop Generation", command=self.stop_generation, state=tk.DISABLED)
        self.stop_button.grid(row=2, column=1, padx=10, pady=10)

    def start_generation(self):
        selected_model_types = [model for model, var in self.model_vars.items() if var.get()]
        selected_project_files = [project for project, var in self.project_vars.items() if var.get()]

        if not selected_model_types or not selected_project_files:
            messagebox.showwarning("Input Error", "Please select at least one model type and one project file.")
            return

        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.thread = threading.Thread(target=self.run_code_generator, args=(selected_model_types, selected_project_files))
        self.thread.start()

    def stop_generation(self):
        self.running = False
        self.stop_button.config(state=tk.DISABLED)
        if self.thread:
            self.thread.join()
        self.start_button.config(state=tk.NORMAL)

    def run_code_generator(self, model_types, project_files):
        print("run_code_generator", model_types, project_files)
        print("dry run", self.dry_run.get())
        for model_type in model_types:
            for project_file in project_files:
                if not self.running:
                    return

                project_name, project_overview, requirements = parse_project_file(os.path.join("Requirements", project_file))
                save_dir_name = f"{project_name}_{model_type}"
                if self.one_shot:
                    save_dir_name = f"{save_dir_name}_one_shot"
                save_dir = os.path.join("Results", save_dir_name)
                os.makedirs(save_dir, exist_ok=True)
                progress_file = os.path.join(save_dir, f"{save_dir_name}.json")

                # Load checkpoint if exists
                if os.path.exists(progress_file):
                    with open(progress_file, 'r') as f:
                        progress = json.load(f)
                else:
                    start_index = 1
                    if self.one_shot:
                        start_index = len(requirements)
                    progress = {"current_req": start_index, "previous_version_dir": "", "info": {}, "one_shot": self.one_shot}

                previous_version_dir = progress.get("previous_version_dir", "")

                for i in range(progress["current_req"], len(requirements) + 1):
                    if not self.running:
                        return

                    # Create the prompt for the AI
                    task_prompt = project_overview + '\n' + '\n'.join(requirements[:i])
                    # Run ChatDev, use default on first run incremental on following runs
                    previous_version_dir, info = run_chat_dev(args, project_name, task_prompt, model_type, previous_version_dir, incremental=((not self.one_shot) and i != 1), dry_run=self.dry_run.get())

                    print(previous_version_dir, info.str)

                    # remove base dir from project to keep file paths under length limit
                    if os.path.exists(os.path.join(previous_version_dir, "base")):
                        shutil.rmtree(os.path.join(previous_version_dir, "base"))

                    copy_dir = os.path.join(save_dir, f"{save_dir_name}_req{i}")
                    if self.one_shot:
                        copy_dir = os.path.join(save_dir, f"{save_dir_name}")


                    # remove previous copy of a conflict exists
                    if os.path.exists(copy_dir):
                        shutil.rmtree(copy_dir)

                    # Copy the result to output dir
                    shutil.copytree(previous_version_dir, copy_dir)

                    # Update checkpoint
                    progress["current_req"] = i + 1
                    progress["previous_version_dir"] = previous_version_dir
                    progress["info"][f"req{i}"] = info.to_dict()
                    pprint(progress)
                    with open(progress_file, 'w') as f:
                        json.dump(progress, f, indent=4)

        self.running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)


def parse_project_file(project_file):
    with open(project_file, 'r') as file:
        lines = file.readlines()
    project_name = lines[0].strip().split(": ")[1]
    project_overview = lines[1].strip().split(": ")[1]
    requirements = [line.strip() for line in lines[2:] if line.strip()]
    return project_name, project_overview, requirements


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='argparse')
    parser.add_argument('--org', type=str, default="DefaultOrganization",
                        help="Name of organization, your software will be generated in WareHouse/name_org_timestamp")
    parser.add_argument('--dry_run', type=str, default="True",
                        help="Dry run, does not call LLMs")
    args = parser.parse_args()

    root = tk.Tk()
    app = CodeGeneratorUI(root, args)
    root.mainloop()

