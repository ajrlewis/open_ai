import os
import sys
import argparse
from dotenv import load_dotenv

sys.path.append("./")
from open_ai.image_bot import ImageBot


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHAT_BOT_SYSTEM = os.getenv("CHAT_BOT_SYSTEM")
CHAT_BOT_TEMPERATURE = os.getenv("CHAT_BOT_TEMPERATURE")


def main(args: argparse.Namespace):
    # Load the image bot prompt from JSON file in data directory if it exists
    filepath = f"{args.data_dir}/image-bot-{args.subject}.json"
    image_bot = ImageBot(api_key=OPENAI_API_KEY)
    image_bot.generate(prompt, style="natural")
    filepath = "data/image-bot-28.png"
    image_bot.write("data/image-bot-28.png")
    os.open("data/image-bot-28.png")


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

# import os
# import sys
# from dotenv import load_dotenv
# from open_ai.image_bot import ImageBot


# load_dotenv()


# def main():
#     OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#     image_bot = ImageBot(api_key=OPENAI_API_KEY)
#     # prompt = "In a cozy living room, Laszlo Hanyecz eagerly types on his computer, offering 10,000 Bitcoins for two pizzas on the Bitcointalk forum. Outside, the evening sky paints a beautiful backdrop. The aroma of freshly baked pizza fills the air as Laszlo awaits the delivery. Finally, a knock on the door reveals a delivery person holding two steaming boxes adorned with the Papa John's logo. This historic exchange of digital currency for real-world goods marks the birth of Bitcoin's utility."
#     # prompt = "In a cozy living room, Laszlo Hanyecz eagerly types on his computer, offering 10,000 Bitcoins for two pizzas on the Bitcointalk forum."
#     prompt = "In a cozy living room, Laszlo Hanyecz eagerly types on his computer, offering 10,000 Bitcoins for two pizzas from Papa Johns on the Bitcointalk forum. Outside the window, the evening sky paints a beautiful backdrop."
#     image_bot.generate(prompt, style="natural")
#     image_bot.write("data/image-bot-28.png")


# if __name__ == "__main__":
#     main()
