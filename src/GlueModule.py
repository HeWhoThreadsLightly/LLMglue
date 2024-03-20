from abc import ABC

from src.GlueLadder import GlueLadder
from src.GlueModel import GlueModel


class GlueModule(ABC):
    def __init__(self, ladder: GlueLadder, index: int):
        self.ladder = ladder
        self.index = index

    def prompt(self, **kwargs):
        raise NotImplemented

    def getGlueModel(self):
        return GlueModel(self)

    def getNext(self):
        return self.ladder.getModule(self.index + 1)

    def start(self):
        pass

