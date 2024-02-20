import os
import sys
import argparse
from dotenv import load_dotenv
import openai

sys.path.append("./")
from open_ai.image_bot import ImageBot


load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")


def main(args: argparse.Namespace):
    # Load the image bot prompt from JSON file in data directory if it exists
    filepath = f"{args.data_dir}/image-bot-{args.subject}.json"
    client = openai.OpenAI(api_key=OPEN_AI_API_KEY)
    image_bot = ImageBot(client=client)
    with open(f"{args.data_dir}/chat-bot-{args.subject}.md") as f:
        prompt = f.read()
        image_bot.generate(prompt, style="natural")
        # image_bot.generate(prompt, style="vivid")
    filepath = f"data/image-bot-{args.subject}-{i}.png"
    while os.path.exists(filepath):
        i += 1
        filepath = f"data/image-bot-{args.subject}-{i}.png"
    image_bot.write(filepath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chat Bot CLI")
    parser.add_argument(
        "--data_dir",
        default="data/",
        help="Data directory containing image bot prompt.",
    )
    parser.add_argument(
        "--subject",
        default="misc",
        help="Subject of the image bot JSON file.",
    )
    args = parser.parse_args()
    main(args)
