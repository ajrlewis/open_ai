from typing import List
from open_ai import OpenAI


class ChatGPT(OpenAI):
    """A ChatGPT class.

    Attributes:
        model: The chat model to use.
        messages: The messages of the chat.
    """

    def __init__(
        self, model: str = "gpt-3.5-turbo", messages: List[str] = [], **kwargs
    ):
        super().__init__(**kwargs)
        self.model = model
        self.messages = messages

    def ask_question(self, question: str) -> str:
        chat_question = {"role": "user", "content": question}
        self.messages.append(chat_question)
        response = self._openai.ChatCompletion.create(
            model=self.model, messages=self.messages
        )
        answer = response.choices[0].message.content
        chat_answer = {"role": "assistant", "content": answer}
        self.messages.append(chat_answer)
        return answer

    def ask_questions(self, questions: List[str]) -> List[str]:
        answers = []
        for question in questions:
            answer = self.ask_question(question=question)
            answers.append(answer)
        return answers

    def to_csv(filename: str):
        headers = ["model", "message_role", "message_content"]

    def from_csv(filename: str):
        pass
