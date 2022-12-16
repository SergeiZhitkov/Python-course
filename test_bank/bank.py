def main():
    greeting = input("Tell your Greeting: ").strip().lower()
    print(value(greeting))



def value(greeting):
    greeting = greeting.lower().strip()
    hello = ""
    for letter in greeting[0:5]:
        hello = hello + letter
    if hello == "hello":
        return "$0"
    elif hello[0] == "h":
        return "$20"
    return "$100"

if __name__ == "__main__":
    main()