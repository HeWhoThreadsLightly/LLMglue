
class ChatHistory:
    def __init__(self):
        self.messages = []

    def add_message(self, message, role="user"):
        self.messages.append({"role": role, "content": message})

    def print(self):
        print(self.messages)

    def copy(self):
        new = ChatHistory()
        new.messages = self.messages[:]
        return new
