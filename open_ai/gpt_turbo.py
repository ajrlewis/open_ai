import csv
import datetime
from typing import Dict, List
from open_ai import OpenAI

Message = Dict[str, str]
Messages = List[Message]
Question = str
Questions = List[Question]
Answer = str
Answers = List[Answer]


class GPTTurbo(OpenAI):
    """A GPTTurbo class.

    https://platform.openai.com/docs/guides/chat/introduction

    Attributes:
        temperature: How random (0.8) or how focused and deterministic (0.2).
        messages: All message of the chat.
        system: The behaviour of the system.
    """

    def __init__(
        self,
        temperature: float = 0.2,
        messages: Messages = [],
        system: str = "You are an assistant to a data engineer. Answer as concisely as possible.",
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.model = "gpt-3.5-turbo"
        self.temperature = temperature
        self.messages = messages
        self.add_message(role="system", content=system)

    def __repr__(self) -> str:
        return f"{self.model} model containing {len(self.messages)} messages."

    def add_message(self, role: str, content: str):
        message = {
            "time": f"{datetime.datetime.now()}",
            "role": role,
            "content": content,
        }
        self.messages.append(message)

    # TODO: catch error if model too large and pass fewer messages.
    def ask_question(self, question: Question) -> Answer:
        time = f"{datetime.datetime.now()}"
        self.add_message(role="user", content=question.strip())
        _messages = [{k: v for k, v in m.items() if k != "time"} for m in self.messages]
        response = self._openai.ChatCompletion.create(
            model=self.model,
            messages=_messages,
            temperature=self.temperature,
        )
        answer = response.choices[0].message.content.strip()
        self.add_message(role="assistant", content=answer)
        return answer

    def ask_questions(self, questions: Questions) -> Answers:
        answers = []
        for question in questions:
            answer = self.ask_question(question=question)
            answers.append(answer)
        return answers

    def pop_first_message(self):
        message = self.messages[0]
        self.messages = self.messages[1:]
        return message

    def pop_last_message(self):
        message = self.messages[-1]
        self.messages = self.messages[:-1]
        return message

    def print(self, last: bool = False):
        messages = self.messages
        if last:
            messages = [messages[-1]]
        print()
        for message in messages:

            if message["role"] == "system":
                start_color = "\033[93m"  # warning
            elif message["role"] == "user":
                start_color = "\033[96m"  # cyan
            elif message["role"] == "assistant":
                start_color = "\033[92m"  # green

            end_color = "\033[0m"
            print(
                start_color,
                message["time"] + " " + message["role"].ljust(10),
                end_color,
            )
            print("." * 30)
            print(start_color, message["content"], end_color)
            print()
        print()

    def to_csv(self, filename: str):
        headers = ["time", "model", "message_role", "message_content"]
        with open(filename, "w", newline="\n") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for message in self.messages:
                writer.writerow(
                    [message["time"], self.model, message["role"], message["content"]]
                )

    def from_csv(self, filename: str):
        pass
