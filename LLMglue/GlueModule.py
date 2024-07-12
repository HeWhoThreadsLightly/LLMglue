from __future__ import annotations
from abc import ABC

from GlueModel import GlueModel


class GlueModule(ABC):
    def __init__(self, ladder: GlueLadder, index: int):
        self.ladder = ladder
        self.index = index

    def prompt(self, **kwargs):
        raise NotImplemented

    def message(self, message):
        raise NotImplemented


    def getGlueModel(self):
        return GlueModel(self)

    def getNext(self):
        return self.ladder.getModule(self.index + 1)


    def token_limit(self):
        return self.getNext().token_limit()

    def start(self):
        pass
