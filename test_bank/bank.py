def main():
    greeting = input("Tell your Greeting: ").strip().lower()
    print(value(greeting))



def value(greeting):
    greeting = greeting.lower().strip()
    words = []
    words = greeting.split(" ")
    word[0] = word[0].replace(",", "")
    if word[0] == "hello":
        return "$0"
    elif word[0] == "h":
        return "$20"
    return "$100"

if __name__ == "__main__":
    main()