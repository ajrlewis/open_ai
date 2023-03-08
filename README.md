# open_ai

A collection of simple classes to access the Open AI suite as a client.

## GPT Turbo

Example Usage:

    from open_ai import GPTTurbo

    OPENAI_API_KEY = "your-api-key"

    gpt = GPTTurbo(api_key=OPENAI_API_KEY)

    answer = gpt.ask_question("Why does the Universe expand?")

    gpt.print()

Example Output:

    2023-03-08 18:46:38.70  system     You are an assistant to a data engineer. Answer as concisely as possible.
    2023-03-08 18:46:38.70  user       Why does the Universe expand?
    2023-03-08 18:46:40.48  assistant  The Universe expands because of the force of dark energy, which causes the rate of expansion to accelerate over time.
