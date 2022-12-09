def main():
    greeting = input("Tell your Greeting: ").strip().lower()
    print(dollar_gives(greeting))



def dollar_gives(g):
    words = g.split(" ")
    p = ""
    for letter in words[0]:
        p = p + letter
    if p == "hello"


if __name__ == "__main__":
    main()