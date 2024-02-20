import os
import sys
import argparse
from dotenv import load_dotenv
import openai

sys.path.append("./")
from open_ai.chat_bot import ChatBot


load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
CHAT_BOT_SYSTEM = os.getenv("OPEN_AI_CHAT_BOT_SYSTEM")
CHAT_BOT_TEMPERATURE = os.getenv("OPEN_AI_CHAT_BOT_TEMPERATURE")


def main(args: argparse.Namespace):
    # Load the chat bot from JSON file in data directory if it exists
    filepath = f"{args.data_dir}/chat-bot-{args.subject}.json"
    client = openai.OpenAI(api_key=OPEN_AI_API_KEY)
    chat_bot = ChatBot.read_json(
        filepath,
        model=args.model,
        temperature=CHAT_BOT_TEMPERATURE,
        system=CHAT_BOT_SYSTEM,
        context_window_size=args.context_window_size,
        client=client,
    )

    # Ask and write the chat bot conversation history to
    if not str(args.print_only).lower() == "true":
        with open(f"{args.data_dir}/chat-bot-{args.subject}.md") as f:
            question = f.read()
            chat_bot.ask(question)
            chat_bot.write_json(filepath)
            chat_bot.context_window_size += 2  # add last question and response

    # Print the chat bot conversation history within the context
    chat_bot.print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chat Bot CLI")
    parser.add_argument(
        "--print_only",
        default=False,
        help="Only print the chat bot conversation history within the context window.",
    )
    parser.add_argument(
        "--data_dir",
        default="data",
        help="Data directory containing chat bot question and chat bot history.",
    )
    parser.add_argument(
        "--subject",
        default="misc",
        help="Subject of the chat bot JSON file.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-3.5-turbo",
        help="Chat bot model to use.",
    )
    parser.add_argument(
        "--context_window_size",
        type=int,
        default=2,
        help="Size of the context window for the chat bot.",
    )
    args = parser.parse_args()
    main(args)
