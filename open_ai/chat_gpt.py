import csv
from typing import List
from open_ai import OpenAI


class ChatGPT(OpenAI):
    """A ChatGPT class.

    Attributes:
        model: The chat model to use.
        messages: The messages of the chat.
        system: The behaviour of the system.
    """

    def __init__(
        self,
        model: str = "gpt-3.5-turbo",
        messages: List[str] = [],
        system: str = "You are a smart assistant.",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.model = model
        self.messages = messages
        self.messages.append({"role": "system", "content": system})

    def ask_question(self, question: str) -> str:
        chat_question = {"role": "user", "content": question.strip()}
        self.messages.append(chat_question)
        response = self._openai.ChatCompletion.create(
            model=self.model, messages=self.messages
        )
        answer = response.choices[0].message.content.strip()
        chat_answer = {"role": "assistant", "content": answer}
        self.messages.append(chat_answer)
        return answer

    def ask_questions(self, questions: List[str]) -> List[str]:
        answers = []
        for question in questions:
            answer = self.ask_question(question=question)
            answers.append(answer)
        return answers

    def to_csv(self, filename: str):
        headers = ["model", "message_role", "message_content"]
        with open(filename, "w", newline="\n") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for message in self.messages:
                writer.writerow([self.model, message["role"], message["content"]])

    def from_csv(self, filename: str):
        pass
