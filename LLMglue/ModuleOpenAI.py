import GlueModel
import os
import openai
import backoff

from openai import OpenAI

from LLMglue.GlueLadder import GlueLadder
from LLMglue.GlueLadder import GlueModule

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
        self.completion_tokens = 0
        self.prompt_tokens = 0

        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4"

    @backoff.on_exception(backoff.expo, openai.OpenAIError)
    def completions_with_backoff(self, **kwargs):
        try:
            return self.client.chat.completions.create(**kwargs)
        except Exception as e:
            print(e)

    def prompt(self, **kwargs):
        result = self.completions_with_backoff(**kwargs)
        # todo log prompt token usage
        return result

    def message(self, message):
        return self.gpt(message)

    def token_limit(self):
        if self.model == "GPT_3_5_TURBO":
            return 16384
        elif self.model == "GPT_3_5_TURBO_NEW":
            return 16384
        elif self.model == "GPT_4":
            return 8192
        elif self.model == "GPT_4_32k":
            return 32768
        elif self.model == "GPT_4_TURBO":
            return 128000

    def gpt(self, prompt, model="gpt-4", temperature=0.7, max_tokens=1000, n=1, stop=None) -> list:
        messages = [{"role": "user", "content": prompt}]
        return self.chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop)

    def chatgpt(self, messages, model="gpt-4", temperature=0.7, max_tokens=1000, n=1, stop=None) -> list:
        outputs = []
        while n > 0:
            cnt = min(n, 20)
            n -= cnt
            res = self.completions_with_backoff(model=model, messages=messages, temperature=temperature, max_tokens=max_tokens,
                                           n=cnt, stop=stop)
            print(res)
            outputs.extend([choice.message.content for choice in res.choices])
            # log completion tokens
            self.completion_tokens += res.usage.completion_tokens
            self.prompt_tokens += res.usage.prompt_tokens
        return outputs

    def gpt_usage(self, backend="gpt-4"):
        if backend == "gpt-4":
            cost = self.completion_tokens / 1000 * 0.06 + self.prompt_tokens / 1000 * 0.03
        elif backend == "gpt-3.5-turbo":
            cost = self.completion_tokens / 1000 * 0.002 + self.prompt_tokens / 1000 * 0.0015
        return {"completion_tokens": self.completion_tokens, "prompt_tokens": self.prompt_tokens, "cost": cost}