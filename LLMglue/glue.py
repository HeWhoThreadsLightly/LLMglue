from ChatDevModule import ModuleChatDev
from ModuleOpenAI import ModuleOpenAI
from ModuleSimpleUI import ModuleSimpleUI
from LLMglue.GlueLadder import GlueLadder

#configuration = [ModuleSimpleUI(None, 0), ModuleOpenAI(None, 1)]
configuration = [ModuleChatDev(None, 0, "T3sting CO limited"), ModuleOpenAI(None, 1)]

ladder = GlueLadder(configuration)  # use default example configuration
c: ModuleChatDev = ladder.modules[0]
c.prompt("Test project", "Make a hello world application")
ladder.start()
