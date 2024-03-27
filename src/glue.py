from ModuleOpenAI import ModuleOpenAI
from ModuleSimpleUI import ModuleSimpleUI
from src.GlueLadder import GlueLadder

configuration = [ModuleSimpleUI(None, 0), ModuleOpenAI(None, 1)]

ladder = GlueLadder(configuration)  # use default example configuration
ladder.start()
