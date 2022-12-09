def main():
    greeting = input("Tell your Greeting: ").strip().lower()
    print(dollar_gives(greeting))



def dollar_gives(g):
    words = g.split(" ")
    p = ""
    for word in words:
        for letter in word[0-5]:
            p = p + letter
    if p == "hello":
        return "$0"
    elif p[0] == "h":
        return "$20"
    return "$100"


if __name__ == "__main__":
    main()