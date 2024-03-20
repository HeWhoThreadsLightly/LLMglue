from src.GlueModule import GlueModule
from src.ModuleOpenAI import ModelOpenAI, ModuleOpenAI
from src.ModuleSimpleUI import ModuleSimpleUI


class GlueLadder:

    def __init__(self, configuration: list[GlueModule] = None):
        if configuration is None:  # use "SimpleUI -> OpenAI" as an example if no configuration is specified
            configuration = [ModuleSimpleUI(self, 0), ModuleOpenAI(self, 1)]
        self.modules: list[GlueModule] = configuration

    def start(self):
        self.modules[0].start()

    def getModule(self, index: int) -> GlueModule:
        if -len(list) <= index < len(list):
            return self.modules[index]
        else:
            raise IndexError
