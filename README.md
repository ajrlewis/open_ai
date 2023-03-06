# open_ai

A collection of simple classes to access the Open AI suite as a client.

## Chat GPT

Example Usage:

    from open_ai import ChatGPT

    chat_gpt = ChatGPT(api_key="your-api-key")

    questions = ["Who was the king of England in 1000 AD?", "What did he die from??"]
    answers = chat_gpt.ask_questions(questions=questions)

    for q, a in zip(questions, answers):
        print(q, "\n", "-" * 80, "\n", a, "\n", "." * 80, "\n",)

Example Output:

    Who was the king of England in 1000 AD?
     --------------------------------------------------------------------------------


    The king of England in 1000 AD was Æthelred the Unready.
     ................................................................................

    Say only his name
     --------------------------------------------------------------------------------
     Æthelred the Unready.
     ................................................................................

    What did he die from??
     --------------------------------------------------------------------------------
     Æthelred the Unready is believed to have died from natural causes, possibly from an illness or old age, in 1016.
     ................................................................................
