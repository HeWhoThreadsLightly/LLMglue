from src.GlueLadder import GlueLadder
from src.GlueModule import GlueModule


class ModuleSimpleUI(GlueModule):
    def __init__(self, ladder: GlueLadder, index: int):
        super().__init__(ladder, index)
        self.model = super().getGlueModel()  # get a reference to the next model for prompting

    def prompt(self, **kwargs):
        pass  # todo make an message list that prompts are appended to

    def start(self):
        try:
            while True:                     # loop until keyboard interrupt
                s = input()                 # get user input
                r = self.model.prompt(s)    # send input to next module
                print(r)                    # print the model response
        except KeyboardInterrupt:
            print('interrupted!')



