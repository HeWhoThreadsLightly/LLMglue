from abc import ABC
from GlueLadder import GlueLadder
from GlueModule import GlueModule

# base wrapper class for calling the next model in the stack
# made to be handed out to module logic code as a substitute to openai.ChatCompletion.create(**kwargs)
# can be overloaded if a module needs it


class GlueModel(ABC):
    def __init__(self, module: GlueModule):
        self.module = module

    def prompt(self, **kwargs):
        return self.module.getNext().prompt(**kwargs)

