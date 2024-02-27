from __future__ import annotations
import json
import os
import time
import openai
from open_ai.open_ai import OpenAI

Message = dict[str, str]
# Messages = list[Message]
# ConversationHistory = list[Messages]
ConversationHistory = list[Message]


class ChatBot(OpenAI):
    """A class to interact with Open AI's Chat GPT model.

    Attributes:
        client: Open AI client to inject
        model: The name of the model.
        temperature: The temperature of the model.
        system: The context system of the chat.
        context_window_size: The window size to use, i.e. number of conversation turns.
        conversation_history: This conversation history.
    References:
        https://platform.openai.com/docs/guides/chat/introduction
        https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability.md
    """

    def __init__(
        self,
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.2,
        system: str = "You are OpenAI's GPT natural language learning model.",
        context_window_size: int = 2,
        conversation_history: ConversationHistory = [],
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.model = str(model)
        self.temperature = float(temperature)
        self._system_message = {}
        self.system = str(system)
        self.context_window_size = int(context_window_size)
        self.conversation_history = conversation_history

    @property
    def system(self) -> str:
        return self._system

    @system.setter
    def system(self, system: str):
        self._system = system
        if system:
            self._system_message = ChatBot.create_message(
                role="system", content=self.system
            )

    def _get_context_messages(self) -> Messages:
        context_messages = [self._system_message] + self.conversation_history[
            len(self.conversation_history) - self.context_window_size :
        ]
        return context_messages

    def _get_answer(self, context_messages: Messages) -> Message:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                temperature=self.temperature,
                messages=context_messages,
            )
            content = response.choices[0].message.content
            answer = ChatBot.create_message(role="assistant", content=content)
        except Exception as e:
            raise e
        else:
            return answer

    def ask(self, question: str) -> str:
        context_messages = self._get_context_messages()  # Get the context messages
        user_question = ChatBot.create_message(role="user", content=question)
        context_messages.append(user_question)
        bot_answer = self._get_answer(context_messages)
        if bot_answer:
            self.conversation_history.append(user_question)
            self.conversation_history.append(bot_answer)
        return bot_answer

    def ask_many(self, questions: List[str]) -> List[str]:
        bot_answers = []
        for question in questions:
            bot_answer = self.ask(question)
            bot_answers.append(bot_answer)
            time.sleep(1)
        return bot_answers

    # def is_conversation_history_empty(self) -> bool:
    #     return len(self.conversation_history) == 0

    # def last_conversation_turn(self):
    #     if self.is_conversation_history_empty:
    #         return []
    #     return self.conversation_history[-1]

    # def last_question(self) -> Opontial[str]:
    #     try:
    #         return self.conversation_history[-1][0]["content"]
    #     except:
    #         return

    # def last_answer(self) -> Opontial[str]:
    #     try:
    #         return self.conversation_history[-1][-1]["content"]
    #     except:
    #         return

    @classmethod
    def tame_short_term_memory(
        cls,
        api_key: str,
        filepath: str = "tame-short-term-memory.json",
    ) -> ChatBot:
        chat = cls.read_json(
            filepath,
            api_key=api_key,
            context_window_size=context_window_size,
        )
        return chat

    def print(self):
        white_color = ""
        print("ChatBot")
        print()
        print(f"Model: {self.model}")
        print(f"Temperature: {self.temperature:.2f}")
        print(f"Context Window Size: {self.context_window_size}")
        print()
        ChatBot._print_message(0, "\033[93m", "system", self._system_message["content"])
        messages = self._get_context_messages()[1:]
        user_messages, bot_messages = messages[::2], messages[1::2]
        for i, (user_message, bot_message) in enumerate(
            zip(user_messages, bot_messages)
        ):
            ChatBot._print_message(
                i * 2 + 1, "\033[95m", "user", user_message["content"]
            )
            ChatBot._print_message(i * 2 + 2, "\033[96m", "bot", bot_message["content"])
        print()

    @staticmethod
    def _print_message(index: int, color: str, role: str, content: str):
        print(f"{color} [{index}] {role}\033[0m: {content}")

    def to_dict(self) -> dict[str, str]:
        data = {
            "model": self.model,
            "temperature": self.temperature,
            "system": self.system,
            "context_window_size": self.context_window_size,
            "conversation_history": self.conversation_history,
        }
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Chat:
        chat = cls(**data)
        return chat

    def to_json(self) -> str:
        data = self.to_dict()
        return json.dumps(data, ensure_ascii=False, indent=4)

    @classmethod
    def from_json(cls, data: str) -> ChatBot:
        chat = cls.from_dict(json.loads(data))
        return chat

    @classmethod
    def read_json(cls, filepath: str, **kwargs) -> ChatBot:
        data = {}
        if os.path.exists(filepath):
            with open(filepath) as f:
                data = json.load(f)
        chat = cls.from_dict(data | kwargs)
        return chat

    def write_json(self, filepath: str):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.to_json())

    @staticmethod
    def create_message(role: str, content: str) -> Message:
        return {"role": role, "content": content.strip()}
