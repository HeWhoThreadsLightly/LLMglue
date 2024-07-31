# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
import argparse
import os
import shutil
import sys
from os.path import isfile, join

from google.protobuf.text_format import ParseBool

from run_chat_dev import run_chat_dev

def parse_project_file(project_file):
    with open(project_file, 'r') as file:
        lines = file.readlines()
    project_name = lines[0].strip().split(": ")[1]
    project_overview = lines[1].strip().split(": ")[1]
    requirements = [line.strip() for line in lines[2:] if line.strip()]
    return project_name, project_overview, requirements

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='argparse')
    parser.add_argument('--id', type=str, default="First",
                        help="Save state in folder Result/{id}/ ")
    parser.add_argument('--org', type=str, default="DefaultOrganization",
                        help="Name of organization, your software will be generated in WareHouse/name_org_timestamp")
    parser.add_argument('--projects', type=str, default="*",
                        help="List of projects to test chat dev on or * for all")
    parser.add_argument('--models', type=str, default="GPT_3_5_TURBO,GPT_4",
                        help="Comma seperated list of GPT Model, choose from {'GPT_3_5_TURBO','GPT_4','GPT_4_32K', 'GPT_4_TURBO'}")
    parser.add_argument('--dry_run', type=str, default="True",
                        help="Dry run, does not call LLMs")
    args = parser.parse_args()

    # parse args

    root_output_folder_name = args.id
    start_dir = os.getcwd()
    save_dir = os.path.join(start_dir, "Results", root_output_folder_name)
    dry_run = ParseBool(args.dry_run)
    if not dry_run:
        print("Not a dry Run!")  # for extra safety during testing running the full suit accidentally would be expencive
        exit(1)

    # Look up and filter project files and models
    project_files_dir = "Requirements"
    model_types = args.models.split(',')
    project_files_found = [f for f in os.listdir(project_files_dir) if isfile(join(project_files_dir, f))]
    project_files = []

    if args.projects == "*":
        project_files = project_files_found
    else:
        project_files = args.projects.split(',')

    print(project_files_found)
    print(model_types)
    print(project_files)

    for model_type in model_types:
        for project_file in project_files:

            # load project requirements
            project_name, project_overview, requirements = parse_project_file(os.path.join(project_files_dir, project_file))

            # Run ChatDev adding one requirement after each iteration
            previous_version_dir = ""
            for i in range(1, len(requirements)):
                # Create the prompt for the AI
                task_prompt = project_overview + '\n'
                task_prompt += '\n'.join(requirements[0:i])

                # Run ChatDev, use default on first run incremental on following runs
                previous_version_dir = run_chat_dev(args, project_name, task_prompt, model_type, previous_version_dir, incremental=(i != 1), dry_run=dry_run)

                # remove base dir from project to keep file paths under length limit
                if os.path.exists(os.path.join(previous_version_dir, "base")):
                    shutil.rmtree(os.path.join(previous_version_dir, "base"))

                # Copy the result to output dir
                copy_dir = os.path.join(save_dir, f"{project_name}_{model_type}", f"{project_name}_{model_type}_req{i}")
                shutil.copytree(previous_version_dir, copy_dir)
