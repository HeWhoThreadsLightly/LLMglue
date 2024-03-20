import GlueModel
import os
import openai
import backoff

from src.GlueLadder import GlueLadder
from src.GlueModule import GlueModule

api_key = os.getenv("OPENAI_API_KEY", "")
if api_key != "":
    openai.api_key = api_key
else:
    print("Warning: OPENAI_API_KEY is not set")

api_base = os.getenv("OPENAI_API_BASE", "")
if api_base != "":
    print("Warning: OPENAI_API_BASE is set to {}".format(api_base))
    openai.api_base = api_base


class ModuleOpenAI(GlueModule):
    def __init__(self, ladder: GlueLadder, index: int):
        super().__init__(ladder, index)

    @backoff.on_exception(backoff.expo, openai.error.OpenAIError)
    def completions_with_backoff(self, **kwargs):
        return openai.ChatCompletion.create(**kwargs)

    def prompt(self, **kwargs):
        result = self.completions_with_backoff(**kwargs)
        # todo log prompt token usage
        return result
