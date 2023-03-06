# open_ai

A simple classes to access the Open AI suite

## Chat GPT

Usage:

    from open_ai import ChatGPT

    chat_gpt = ChatGPT(api_key="your-api-key")

    questions = ["Who was the king of England in 1000 AD?", "What did he die from??"]
    answers = chat_gpt.ask_questions(questions=questions)
    
    for q, a in zip(questions, answers):
        print(q)
        print("-" * 80)
        print(a)
        print("-" * 80)
        print("-" * 80)

