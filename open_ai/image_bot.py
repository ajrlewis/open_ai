from __future__ import annotations
from base64 import b64decode
from open_ai.open_ai import OpenAI


class ImageBot(OpenAI):
    def __init__(self, model: str = "dall-e-2", **kwargs):
        """A class to interact with Open AI's Dall-E model.

        Attributes:
            model: The name of the model.
            temperature: The temperature of the model.
        References:
        """

        super().__init__(**kwargs)
        self.model = model
        self.data = bytes()

    def generate(self, prompt: str, size: str = "1024x1024", style: str = "vivid"):
        response = self.client.images.generate(
            model=self.model,
            prompt=prompt,
            size=size,
            response_format="b64_json",
            n=1,
            style=style,
        )
        self.data = b64decode(response.data[0].b64_json)

    # def edit(
    #     self,
    #     image_data: bytes,
    #     mask_data: bytes,
    #     prompt: str,
    #     size: str,
    # ):
    #     response = self.client.Image.create_edit(
    #         image=image_data,
    #         mask=mask_data,
    #         prompt=prompt,
    #         n=1,
    #         size=size,
    #     )
    #     self.data = self._data_from_response(response)

    @staticmethod
    def read(filename: str) -> bytes:
        with open(filename, "rb") as f:
            data = f.read()
        return data

    def write(self, filename: str):
        with open(filename, "wb") as f:
            f.write(self.data)
