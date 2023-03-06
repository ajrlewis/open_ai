import openai
import requests


class OpenAI:
    def __init__(self, api_key: str):
        self._openai = openai
        self._openai.api_key = api_key
        self.model = "gpt-3.5-turbo"
        self.messages = []
        self.images = []

    def get_image(self, prompt: str, size: str) -> str:
        try:
            response = openai.Image.create(
                prompt=prompt,
                size=size,
                n=1,
            )
            image_url = response["data"][0]["url"]
            response = requests.get(image_url)  # get image from url
            with open(f"data/{prompt}.png", "wb") as f:
                f.write(response.content)
        except openai.error.OpenAIError as e:
            print(e.http_status)
            print(e.error)
        else:
            return image_url


def main():

    import os
    from dotenv import load_dotenv

    load_dotenv()

    API_KEY = os.getenv("OPENAI_API_KEY")

    open_ai = OpenAI(api_key=API_KEY)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                # "role": "user",
                "role": "assistant",
                "content": "Tell the world about the ChatGPT API in the style of a pirate.",
            }
        ],
    )

    print("-" * 80)
    print(completion)
    print("-" * 80)
    print(completion.choices)
    print("-" * 80)
    print(completion.choices[0].message.content)
    print("-" * 80)

    # messages = [
    #  {"role": "system", "content" : "You’re a kind helpful assistant"}
    # ]

    # import openai

    # content = input("User: ")
    # messages.append({"role": "user", "content": content})

    # completion = openai.ChatCompletion.create(
    #   model="gpt-3.5-turbo",
    #   messages=messages
    # )

    # chat_response = completion.choices[0].message.content
    # print(f'ChatGPT: {chat_response}')

    # while True:
    #     content = input("User: ")
    #     messages.append({"role": "user", "content": content})

    #     completion = openai.ChatCompletion.create(
    #       model="gpt-3.5-turbo",
    #       messages=messages
    #     )

    #     chat_response = completion.choices[0].message.content
    #     print(f'ChatGPT: {chat_response}')
    #     messages.append({"role": "assistant", "content": chat_response})


if __name__ == "__main__":
    main()
