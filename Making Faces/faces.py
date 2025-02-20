def main():
    emojis()

def emojis():
    emoji = input("Enter an emoji expression: ")
    new_emoji = emoji.replace(":)", "🙂").replace(":(", "🙁")
    print(new_emoji)

main()
