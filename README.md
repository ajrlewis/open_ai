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
     The king of England in 1000 AD was Æthelred II, also known as Æthelred the Unready.
     ................................................................................

    What did he die from??
     --------------------------------------------------------------------------------
     Æthelred II died on April 23, 1016, possibly from natural causes, although there are some accounts that suggest that he was murdered.
     ................................................................................

