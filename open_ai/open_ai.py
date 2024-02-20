import openai


class OpenAI:
    """A class to interact with Open AI's python client.

    Attributes:
        client: OpenAI client dependency to inject.
    References:
        https://github.com/openai/openai-python
    """

    def __init__(self, client: openai.OpenAI):
        self.client = client
