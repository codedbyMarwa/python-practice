def convert(text):
    # Replace emoticons with emoji
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_input = input("Enter some text: ")
    converted_text = convert(user_input)
    print(converted_text)

if __name__== "__main__":
    main()
