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

     2023-03-10 16:41:10.661301 system
    ..............................
     You are an assistant to a data engineer. Answer as concisely as possible.

     2023-03-10 16:41:10.661319 user
    ..............................
     Why does the Universe expand?

     2023-03-10 16:41:12.130370 assistant
    ..............................
     The Universe expands because of the Big Bang, which caused a rapid expansion of space-time in all directions.

