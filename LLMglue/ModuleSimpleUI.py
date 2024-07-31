from ChatHistory import ChatHistory
from LLMglue.GlueLadder import GlueLadder
from LLMglue.GlueModule import GlueModule



class ModuleSimpleUI(GlueModule):
    def __init__(self, ladder: GlueLadder, index: int):
        super().__init__(ladder, index)
        self.model = super().getGlueModel()  # get a reference to the next model for prompting
        self.history = ChatHistory()  # initialize an empty list to store the chat history

    def prompt(self, **kwargs):
        pass  # todo make an message list that prompts are appended to

    def start(self):
        try:
            while True:                     # loop until keyboard interrupt
                prompt = input()                 # get user input
                self.history.add_message(prompt)
                r = self.model.message(self.history)  # send input to next module
                self.history.print()
                print(r)                    # print the model response
        except KeyboardInterrupt:
            print('interrupted!')


if __name__ == "__main__":
    from ModuleOpenAI import ModuleOpenAI
    configuration = [ModuleSimpleUI(None, 0), ModuleOpenAI(None, 1)]
    ladder = GlueLadder(configuration)  # use default example configuration
    ladder.start()