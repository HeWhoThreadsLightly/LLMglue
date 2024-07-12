from __future__ import annotations
from abc import ABC

# base wrapper class for calling the next model in the stack
# made to be handed out to module logic code as a substitute to openai.ChatCompletion.create(**kwargs)
# can be overloaded if a module needs it


class GlueModel(ABC):
    def __init__(self, module: GlueModule):
        self.module = module

    def prompt(self, **kwargs):
        return self.module.getNext().prompt(**kwargs)

    def message(self, message):
        return self.module.getNext().message(message)

    def token_limit(self):
        return self.module.getNext().token_limit()

