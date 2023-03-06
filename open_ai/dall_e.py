from typing import List
from open_ai import OpenAI
import requests


class DallE(OpenAI):
    """A Dall-E class."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def image(
        self, description: str, size: str = "1024x1024", should_write: bool = True
    ) -> str:
        """Generates a DALL-E image given a description.

        Args:
            description: A description of the image that you want generated.
            size: The size of the image in pixels to generate.
            should_write: Save the image as a PNG file in the current directory?
        Returns:
            The byte data of the image.
        """
        image_url = self._image_url(prompt=description, size=size)
        image_data = requests.get(image_url).content  # get image data from URL
        if should_write:
            image_filename = description.replace(" ", "-").lower()[:21] + ".png"
            self._write_image(data=image_data, filename=image_filename)
        return image_data

    def _image_url(self, prompt: str, size: str) -> str:
        response = self._openai.Image.create(
            prompt=prompt,
            size=size,
            n=1,
        )
        image_url = response["data"][0]["url"]
        return image_url

    def _write_image(self, data, filename: str):
        with open(filename, "wb") as f:
            f.write(data)

    def to_csv(filename: str):
        headers = ["image_data"]

    def from_csv(filename: str):
        pass


def main():

    import os
    from dotenv import load_dotenv

    load_dotenv()

    API_KEY = os.getenv("OPENAI_API_KEY")

    dall_e = DallE(api_key=API_KEY)
    dall_e.image(description="A black and white corgi dog.")


if __name__ == "__main__":
    main()
