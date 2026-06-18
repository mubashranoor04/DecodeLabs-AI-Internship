def show_help():
    print("""
Bot: Here are the commands I understand:

- hello / hi / hey
- how are you
- what is your name
- who made you
- what is your goal
- what can you do
- what is decodelabs
- thank you
- help
- exit / quit / bye
""")


def get_response(user_input):

    if user_input in ['hello', 'hi', 'hey', 'wassup']:
        return "Hello! Nice to meet you."

    elif 'how are you' in user_input:
        return "I am functioning perfectly. Thanks for asking!"

    elif 'your name' in user_input or 'who are you' in user_input:
        return "I am DecodeBot, a Rule-Based AI Chatbot."

    elif 'made you' in user_input or 'creator' in user_input:
        return "I was created by an AI Intern as part of DecodeLabs Project 1."

    elif 'goal' in user_input:
        return "My goal is to assist users and demonstrate rule-based artificial intelligence."

    elif 'what can you do' in user_input:
        return "I can answer simple predefined questions using decision-making logic."

    elif 'decodelabs' in user_input:
        return "DecodeLabs helps aspiring engineers build practical AI skills through projects."

    elif 'thank' in user_input:
        return "You're welcome! Happy to help."

    elif 'help' in user_input:
        show_help()
        return None

    else:
        return "I don't understand that yet. Type 'help' to see available commands."


def main():

    print("=" * 50)
    print("DecodeBot Activated")
    print("Rule-Based AI Chatbot - Project 1")
    print("Type 'help' to see available commands.")
    print("Type 'exit' to quit.")
    print("=" * 50)

    message_count = 0

    while True:

        user_input = input("\nYou: ").lower().strip()

        if user_input in ['exit', 'quit', 'bye', 'goodbye']:
            print(f"\nBot: Goodbye! We exchanged {message_count} messages today.")
            break

        message_count += 1

        response = get_response(user_input)

        if response:
            print("Bot:", response)


if __name__ == "__main__":
    main()