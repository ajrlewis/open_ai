from typing import List
import openai
import requests


class OpenAI:
    """An open AI class representation,"""

    def __init__(self, api_key: str):
        self._openai = openai
        self._openai.api_key = api_key


def main():

    import os
    from dotenv import load_dotenv

    load_dotenv()

    API_KEY = os.getenv("OPENAI_API_KEY")
    open_ai = OpenAI(api_key=API_KEY)

    print(open_ai)


if __name__ == "__main__":
    main()
