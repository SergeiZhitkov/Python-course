import emoji

message = input("Enter a message: ").strip()

print(emoji.emojize(message, language='alias'))