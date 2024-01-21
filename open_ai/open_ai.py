import openai


class OpenAI:
    """A class to interact with Open AI's python client.

    Attributes:
        api_key: Your API key for Open AI.
    References:
        https://github.com/openai/openai-python
    """

    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)
