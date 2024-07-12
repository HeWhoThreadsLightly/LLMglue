import logging
import os
import sys

from GlueLadder import GlueLadder
from GlueModule import GlueModule
from camel.typing import ModelType
from chatdev import ChatDevGlueModelGlobal
from chatdev.chat_chain import ChatChain


class ModuleChatDev(GlueModule):
    def __init__(self, ladder: GlueLadder, index: int, company: str):
        super().__init__(ladder, index)
        self.path = None
        self.company = company
        self.config_path = None
        self.config_phase_path = None
        self.config_role_path = None
        ChatDevGlueModelGlobal.set(self.getGlueModel())

        root = os.path.dirname(os.path.dirname(__file__))
        self.chatDevRoot = os.path.join(root, "ChatDev")
        sys.path.append(self.chatDevRoot)
        config_dir = os.path.join(self.chatDevRoot, "CompanyConfig", self.company)
        default_config_dir = os.path.join(self.chatDevRoot, "CompanyConfig", "Default")

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

        self.config_path, self.config_phase_path, self.config_role_path = tuple(config_paths)

    def prompt(self, project_name, task_prompt, org_name="DefaultOrganization"):

        chat_chain = ChatChain(config_path=self.config_path,
                               config_phase_path=self.config_phase_path,
                               config_role_path=self.config_role_path,
                               task_prompt=task_prompt,
                               project_name=project_name,
                               org_name=org_name,
                               model_type=ModelType.LLM_GLUE,
                               code_path=self.path)
        chat_chain.GlueModel = self.getGlueModel()
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

