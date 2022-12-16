def main():
    greeting = input("Tell your Greeting: ").strip().lower()
    print(value(greeting))



def value(greeting):
    greeting = greeting.lower().strip()
    words = []
    words = greeting.split(" ")
    words[0] = words[0].replace(",", "")
    if words[0] == "hello":
        return "$0"
    elif words[0][0] == "h":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()