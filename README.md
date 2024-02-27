# Open AI

![My Package Logo](images/logo.png)

## Installation

Install via pip:

```bash
pip install git+https://github.com/ajrlewis/open_ai.git
```

or clone the repository, create a virtual environment and install the dependencies:

```bash
git clone https://github.com/ajrlewis/open_ai.git
cd open_ai
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

Create an `.env` file with your API key:

```bash
OPEN_AI_APIKEY="your-api-key"
```

```python
import os
from dotenv import load_dotenv
import openai
from open_ai.chat_bot import ChatBot


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPEN_AI_API_KEY)

bot = ChatBot(
    model="gpt-3.5-turbo",
    temperature=0.2,
    system="You are Open AI's Chat GPT natural language learning model.",
    context_window_size=2,
    client=client,
)

bot.ask("Hello World!")
bot.print()
```

Prints the following to the terminal:

```
ChatBot

Model: gpt-3.5-turbo
Temperature: 0.20
Context Window Size: 2

[0] system: You are Open AI's Chat GPT natural language learning model.
[1] user: Hello World!
[2] bot: Hello! How can I assist you today?

bot.write_json("hello-world.json")
```

whilst

```python
bot.write_json("hello-world.json")
```

creates a JSON file whose contents looks like this:

```json
{
    "model": "gpt-3.5-turbo",
    "temperature": 0.2,
    "system": "You are Open AI's Chat GPT natural language learning model.",
    "context_window_size": 2,
    "conversation_history": [
        {
            "role": "user",
            "content": "Hello World!"
        },
        {
            "role": "assistant",
            "content": "Hello! How can I assist you today?"
        }
    ]
}
```

### Command Line

Add these additional variables to your `.env` file:

```bash
CHAT_BOT_SYSTEM="You are Open AI's Chat GPT natural language learning model."
CHAT_BOT_TEMPERATURE=0.2
```

A markdown document in a `data` directory is expected with the question you want to ask, e.g.  `data/hello-world.md`:

```markdown
Hello world!
```

The following command line usage:

```bash
python3 scripts/chat_bot_cli.py --subject hello-world --context_window_size 2
```

will print and write the same as above and save the output to `data/hello-world.json`.

## License

This package is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
