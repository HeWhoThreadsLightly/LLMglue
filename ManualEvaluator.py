import threading

import tkinter as tk


class ManualEvaluatorUI:
    def __init__(self, root, project_name, model_type, save_dir):
        self.root = root
        self.root.title(f"Manual Evaluator - {project_name} ({model_type})")

        self.project_name = project_name
        self.model_type = model_type
        self.save_dir = save_dir
        self.current_req = 0
        self.total_reqs = 0
        self.evaluation_results = []

        self.load_checkpoint()
        self.create_widgets()
        self.update_ui()

    def load_checkpoint(self):
        checkpoint_file = os.path.join(self.save_dir, f"{self.project_name}_{self.model_type}.json")
        if os.path.exists(checkpoint_file):
            with open(checkpoint_file, 'r') as f:
                progress = json.load(f)
                self.current_req = progress["current_req"]
                self.evaluation_results = progress.get("evaluation_results", [])
        else:
            self.evaluation_results = []

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text=f"Project: {self.project_name}")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.description_label = tk.Label(self.root, text=f"Model Type: {self.model_type}")
        self.description_label.grid(row=1, column=0, padx=10, pady=10)

        self.requirements_frame = tk.Frame(self.root)
        self.requirements_frame.grid(row=2, column=0, padx=10, pady=10)

        self.progress_label = tk.Label(self.root, text="")
        self.progress_label.grid(row=3, column=0, padx=10, pady=10)

        self.done_button = tk.Button(self.root, text="Done", command=self.next_evaluation)
        self.done_button.grid(row=4, column=0, padx=10, pady=10)

    def update_ui(self):
        for widget in self.requirements_frame.winfo_children():
            widget.destroy()

        requirements = self.load_requirements()

        self.total_reqs = len(requirements)
        self.progress_label.config(text=f"Progress: {self.current_req}/{self.total_reqs}")

        for i, req in enumerate(requirements):
            state = self.evaluation_results[i] if i < len(self.evaluation_results) else "Not Evaluated"
            label = tk.Label(self.requirements_frame, text=req)
            label.grid(row=i, column=0, padx=10, pady=5)

            var = tk.StringVar(value=state)
            cb = ttk.Combobox(self.requirements_frame, textvariable=var, values=["Not Evaluated", "No", "Yes"])
            cb.grid(row=i, column=1, padx=10, pady=5)
            cb.bind("<<ComboboxSelected>>", lambda event, idx=i: self.update_evaluation(idx, event.widget.get()))

    def update_evaluation(self, idx, value):
        if len(self.evaluation_results) <= idx:
            self.evaluation_results.extend(["Not Evaluated"] * (idx - len(self.evaluation_results) + 1))
        self.evaluation_results[idx] = value

    def next_evaluation(self):
        self.current_req += 1
        if self.current_req >= self.total_reqs:
            messagebox.showinfo("Evaluation Complete", "All requirements have been evaluated.")
            self.save_checkpoint()
            self.root.quit()
        else:
            self.save_checkpoint()
            self.update_ui()

    def save_checkpoint(self):
        checkpoint_file = os.path.join(self.save_dir, f"{self.project_name}_{self.model_type}.json")
        progress = {
            "current_req": self.current_req,
            "evaluation_results": self.evaluation_results
        }
        with open(checkpoint_file, 'w') as f:
            json.dump(progress, f)

    def load_requirements(self):
        project_file = os.path.join("Requirements", f"{self.project_name}.txt")
        with open(project_file, 'r') as file:
            lines = file.readlines()
        requirements = [line.strip() for line in lines[2:] if line.strip()]
        return requirements

    def run_shell_script(self):
        copy_dir = os.path.join(self.save_dir, f"{self.project_name}_{self.model_type}_req{self.current_req}")
        manual_md_path = os.path.join(copy_dir, "manual.md")

        # Open manual.md in a window
        manual_window = tk.Toplevel(self.root)
        manual_window.title("Manual Evaluation")
        manual_text = tk.Text(manual_window)
        with open(manual_md_path, 'r') as f:
            manual_text.insert(tk.END, f.read())
        manual_text.pack()

        # Run shell script
        script = f"""
        conda remove --name tmp_env --all -y
        conda create --name tmp_env python=3.8 -y
        conda activate tmp_env
        pip install -r {os.path.join(copy_dir, 'requirements.txt')}
        python {os.path.join(copy_dir, 'main.py')}
        """
        process = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_window = tk.Toplevel(self.root)
        output_window.title("Shell Script Output")
        output_text = tk.Text(output_window)
        output_text.pack()

        def read_output():
            while True:
                line = process.stdout.readline()
                if not line:
                    break
                output_text.insert(tk.END, line)
            process.stdout.close()

        threading.Thread(target=read_output).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = ManualEvaluatorUI(root, "example_project", "GPT_4", "Results")
    root.mainloop()
