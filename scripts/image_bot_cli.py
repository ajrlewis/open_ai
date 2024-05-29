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
    with open(f"{args.data_dir}/image-bot-{args.subject}.md") as f:
        prompt = f.read()
        print(f"{prompt = }")
        image_bot.generate(prompt, style=args.style)

    # Get image filename and save
    base_filepath = f"data/image-bot-{args.subject}"
    for i in range(100):
        filepath = f"{base_filepath}-{i}.png"
        if os.path.exists(filepath):
            continue
        else:
            break
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
    parser.add_argument(
        "--style",
        default="vivid",
        help="Style of the image; natural or vivid.",
    )
    args = parser.parse_args()
    main(args)
