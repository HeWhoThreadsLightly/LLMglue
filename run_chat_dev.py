import logging
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from pprint import pprint

import numpy as np

from camel.typing import ModelType
from chatdev.chat_chain import ChatChain
from chatdev.statistics import prompt_cost

root = os.path.join(os.path.dirname(__file__), "ChatDev")
sys.path.append(root)


try:
    from openai.types.chat.chat_completion_message_tool_call import ChatCompletionMessageToolCall
    from openai.types.chat.chat_completion_message import FunctionCall

    openai_new_api = True  # new openai api version
except ImportError:
    openai_new_api = False  # old openai api version
    print(
        "Warning: Your OpenAI version is outdated. \n "
        "Please update as specified in requirement.txt. \n "
        "The old API interface is deprecated and will no longer be supported.")


def get_config(company):
    """
    return configuration json files for ChatChain
    user can customize only parts of configuration json files, other files will be left for default
    Args:
        company: customized configuration name under CompanyConfig/

    Returns:
        path to three configuration jsons: [config_path, config_phase_path, config_role_path]
    """
    config_dir = os.path.join(root, "CompanyConfig", company)
    default_config_dir = os.path.join(root, "CompanyConfig", "Default")

    config_files = [
        "ChatChainConfig.json",
        "PhaseConfig.json",
        "RoleConfig.json"
    ]

    config_paths = []

    for config_file in config_files:
        company_config_path = os.path.join(config_dir, config_file)
        default_config_path = os.path.join(default_config_dir, config_file)

        if os.path.exists(company_config_path):
            config_paths.append(company_config_path)
        else:
            config_paths.append(default_config_path)

    return tuple(config_paths)


class Info:
    def __init__(self):
        self.model_type = ""
        self.str = ""
        self.cost = -1
        self.version_updates = -1
        self.num_code_files = -1
        self.num_png_files = -1
        self.num_doc_files = -1
        self.code_lines = -1
        self.env_lines = -1
        self.manual_lines = -1
        self.duration = -1
        self.num_utterance = -1
        self.num_reflection = -1
        self.num_prompt_tokens = -1
        self.num_completion_tokens = -1
        self.num_total_tokens = -1
        self.start_time = -1
        self.end_time = -1

    def to_dict(self):
        return {
            "model_type": self.model_type,
            "str": self.str,
            "cost": self.cost,
            "version_updates": self.version_updates,
            "num_code_files": self.num_code_files,
            "num_png_files": self.num_png_files,
            "num_doc_files": self.num_doc_files,
            "code_lines": self.code_lines,
            "env_lines": self.env_lines,
            "manual_lines": self.manual_lines,
            "duration": self.duration,
            "num_utterance": self.num_utterance,
            "num_reflection": self.num_reflection,
            "num_prompt_tokens": self.num_prompt_tokens,
            "num_completion_tokens": self.num_completion_tokens,
            "num_total_tokens": self.num_total_tokens
            #"start_time": self.start_time,
            #"end_time": self.end_time,
        }

def get_info(dir, log_filepath):
    print("dir:", dir)
    info = Info()

    if os.path.exists(dir):
        filenames = os.listdir(dir)
        # print(filenames)

        info.num_code_files = len([filename for filename in filenames if filename.endswith(".py")])
        # print("num_code_files:", info.num_code_files)

        info.num_png_files = len([filename for filename in filenames if filename.endswith(".png")])
        # print("num_png_files:", info.num_png_files)

        info.num_doc_files = 0
        for filename in filenames:
            if filename.endswith(".py") or filename.endswith(".png"):
                continue
            if os.path.isfile(os.path.join(dir, filename)):
                # print(filename)
                info.num_doc_files += 1
        # print("num_doc_files:", info.num_doc_files)

        if "meta.txt" in filenames:
            lines = open(os.path.join(dir, "meta.txt"), "r", encoding="utf8").read().split("\n")
            info.version_updates = float([lines[i + 1] for i, line in enumerate(lines) if "Code_Version" in line][0]) + 1
        else:
            info.version_updates = -1
        # print("version_updates: ", info.version_updates)

        if "requirements.txt" in filenames:
            lines = open(os.path.join(dir, "requirements.txt"), "r", encoding="utf8").read().split("\n")
            info.env_lines = len([line for line in lines if len(line.strip()) > 0])
        else:
            info.env_lines = -1
        # print("env_lines:", info.env_lines)

        if "manual.md" in filenames:
            lines = open(os.path.join(dir, "manual.md"), "r", encoding="utf8").read().split("\n")
            info.manual_lines = len([line for line in lines if len(line.strip()) > 0])
        else:
            info.manual_lines = -1
        # print("manual_lines:", info.manual_lines)

        info.code_lines = 0
        for filename in filenames:
            if filename.endswith(".py"):
                # print("......filename:", filename)
                lines = open(os.path.join(dir, filename), "r", encoding="utf8").read().split("\n")
                info.code_lines += len([line for line in lines if len(line.strip()) > 0])
        # print("code_lines:", info.code_lines)

        lines = open(log_filepath, "r", encoding="utf8").read().split("\n")
        sublines = [line for line in lines if "| **model_type** |" in line]
        if len(sublines) > 0:
            model_type = sublines[0].split("| **model_type** | ModelType.")[-1].split(" | ")[0]
            model_type = model_type[:-2]
            if model_type == "GPT_3_5_TURBO" or model_type == "GPT_3_5_TURBO_NEW":
                model_type = "gpt-3.5-turbo"
            elif model_type == "GPT_4":
                model_type = "gpt-4"
            elif model_type == "GPT_4_32k":
                model_type = "gpt-4-32k"
            elif model_type == "GPT_4_TURBO":
                model_type = "gpt-4-1106-preview"
            else:
                info.model_type = f"Unidentified({model_type})"
            if info.model_type == "":
                info.model_type = model_type
            # print("model_type:", info.model_type)

        lines = open(log_filepath, "r", encoding="utf8").read().split("\n")
        start_lines = [line for line in lines if "**[Start Chat]**" in line]
        chat_lines = [line for line in lines if "<->" in line]
        info.num_utterance = len(start_lines) + len(chat_lines)
        # print("num_utterance:", info.num_utterance)

        lines = open(log_filepath, "r", encoding="utf8").read().split("\n")
        sublines = [line for line in lines if line.startswith("prompt_tokens:")]
        if len(sublines) > 0:
            nums = [int(line.split(": ")[-1]) for line in sublines]
            info.num_prompt_tokens = np.sum(nums)
            # print("num_prompt_tokens:", info.num_prompt_tokens)

        lines = open(log_filepath, "r", encoding="utf8").read().split("\n")
        sublines = [line for line in lines if line.startswith("completion_tokens:")]
        if len(sublines) > 0:
            nums = [int(line.split(": ")[-1]) for line in sublines]
            info.num_completion_tokens = np.sum(nums)
            # print("num_completion_tokens:", info.num_completion_tokens)

        lines = open(log_filepath, "r", encoding="utf8").read().split("\n")
        sublines = [line for line in lines if line.startswith("total_tokens:")]
        if len(sublines) > 0:
            nums = [int(line.split(": ")[-1]) for line in sublines]
            info.num_total_tokens = np.sum(nums)
            # print("num_total_tokens:", info.num_total_tokens)

        lines = open(log_filepath, "r", encoding="utf8").read().split("\n")
        info.num_reflection = 0
        for line in lines:
            if "on : Reflection" in line:
                info.num_reflection += 1
        # print("num_reflection:", info.num_reflection)

    info.cost = 0.0
    if info.num_png_files != -1:
        info.cost += info.num_png_files * 0.016
    if not info.model_type.startswith("Unidentified("):
        if prompt_cost(info.model_type, info.num_prompt_tokens, info.num_completion_tokens) != -1:
            info.cost += prompt_cost(info.model_type, info.num_prompt_tokens, info.num_completion_tokens)

    pattern = re.compile(r'\b(Starts|Ends) \((\d+)\)')
    lines = open(log_filepath, "r", encoding="utf8").read().split("\n")
    sublines = [line for line in lines if line.startswith("ChatDev Starts (")]
    if len(sublines) > 0:
        nums = []
        for line in sublines:
            matches = pattern.search(line)
            if matches:
                n = matches.groups()[-1]
                info.start_time = datetime.strptime(n, "%Y%m%d%H%M%S")

    lines = open(log_filepath, "r", encoding="utf8").read().split("\n")
    sublines = [line for line in lines if line.startswith("ChatDev Ends (")]
    if len(sublines) > 0:
        nums = []
        for line in sublines:
            matches = pattern.search(line)
            if matches:
                n = matches.groups()[-1]
                info.end_time = datetime.strptime(n, "%Y%m%d%H%M%S")


    # Calculate the duration
    if info.end_time != -1 and  info.start_time != -1:
        info.duration = info.end_time - info.start_time
        info.duration = info.duration.total_seconds()
    else:
        info.duration = -1
    print(info.duration)
    # print("duration:", info.duration)

    # info = f"🕑duration={duration}s 💰cost=${cost} 🔨version_updates={version_updates} 📃num_code_files={num_code_files} 🏞num_png_files={num_png_files} 📚num_doc_files={num_doc_files} 📃code_lines={code_lines} 📋env_lines={env_lines} 📒manual_lines={manual_lines} 🗣num_utterances={num_utterance} 🤔num_self_reflections={num_reflection} ❓num_prompt_tokens={num_prompt_tokens} ❗num_completion_tokens={num_completion_tokens} ⁉️num_total_tokens={num_total_tokens}"

    info.str = "\n\n💰**cost**=${:.6f}\n\n🔨**version_updates**={}\n\n📃**num_code_files**={}\n\n🏞**num_png_files**={}\n\n📚**num_doc_files**={}\n\n📃**code_lines**={}\n\n📋**env_lines**={}\n\n📒**manual_lines**={}\n\n🗣**num_utterances**={}\n\n🤔**num_self_reflections**={}\n\n❓**num_prompt_tokens**={}\n\n❗**num_completion_tokens**={}\n\n🌟**num_total_tokens**={}\n\n🕑**duration**={}s" \
        .format(info.cost,
                info.version_updates,
                info.num_code_files,
                info.num_png_files,
                info.num_doc_files,
                info.code_lines,
                info.env_lines,
                info.manual_lines,
                info.num_utterance,
                info.num_reflection,
                info.num_prompt_tokens,
                info.num_completion_tokens,
                info.num_total_tokens,
                info.duration
    )

    return info

def run_chat_dev(args, project_name, task_prompt, model_type, code_path, incremental: bool, dry_run: bool=False):
    config = ["Default", "Incremental"][incremental]
    config_path, config_phase_path, config_role_path = get_config(config)
    # Start ChatDev

    # ----------------------------------------
    #          Init ChatChain
    # ----------------------------------------

    args2type = {'GPT_3_5_TURBO': ModelType.GPT_3_5_TURBO,
                 'GPT_4': ModelType.GPT_4,
                 'GPT_4_32K': ModelType.GPT_4_32k,
                 'GPT_4_TURBO': ModelType.GPT_4_TURBO,
                 'GPT_4_TURBO_V': ModelType.GPT_4_TURBO_V
                 }
    if openai_new_api:
        args2type['GPT_3_5_TURBO'] = ModelType.GPT_3_5_TURBO_NEW

    chat_chain = ChatChain(config_path=config_path,
                           config_phase_path=config_phase_path,
                           config_role_path=config_role_path,
                           task_prompt=task_prompt,
                           project_name=project_name,
                           org_name=args.org,
                           model_type=args2type[model_type],
                           code_path=code_path)

    # ----------------------------------------
    #          Init Log
    # ----------------------------------------
    logging.basicConfig(filename=chat_chain.log_filepath, level=logging.INFO,
                        format='[%(asctime)s %(levelname)s] %(message)s',
                        datefmt='%Y-%d-%m %H:%M:%S', encoding="utf-8")


    # ----------------------------------------
    #          Pre Processing
    # ----------------------------------------

    chat_chain.pre_processing()
    dir_name = "_".join([chat_chain.project_name, chat_chain.org_name, chat_chain.start_time])
    software_path = os.path.join(root, "WareHouse", dir_name)

    if dry_run:
        Path(chat_chain.log_filepath).touch()
        with open(os.path.join(software_path, "main.py"), "w") as code:
            code.write("print('Hello world')")
        chat_chain.post_processing()
        return software_path, get_info(software_path, os.path.join(software_path, f"{dir_name}.log"))

    # ----------------------------------------
    #          Personnel Recruitment
    # ----------------------------------------

    chat_chain.make_recruitment()

    # ----------------------------------------
    #          Chat Chain
    # ----------------------------------------

    chat_chain.execute_chain()

    # ----------------------------------------
    #          Post Processing
    # ----------------------------------------

    chat_chain.post_processing()

    return software_path, get_info(software_path, os.path.join(software_path, f"{dir_name}.log"))


if __name__ == "__main__":
    dir_path = os.path.join("Results", "First", "FOCM_GPT_3_5_TURBO", "QRCodeGenerator", "QRCodeGenerator_THUNLP_20231015214731")
    info = get_info(dir_path, os.path.join(dir_path, "QRCodeGenerator_THUNLP_20231015214731.log"))
    print(info.str)