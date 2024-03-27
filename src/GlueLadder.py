from GlueModule import GlueModule


class GlueLadder:

    def __init__(self, configuration: list[GlueModule] = None):
        for m in configuration:
            m.ladder = self

        self.modules: list[GlueModule] = configuration

    def start(self):
        self.modules[0].start()

    def getModule(self, index: int) -> GlueModule:
        if -len(self.modules) <= index < len(self.modules):
            return self.modules[index]
        else:
            raise IndexError
