def main():
    greeting = input("Tell your Greeting: ").strip().lower()
    print(dollar_gives(greeting))



def dollar_gives(g):
    words = g.split(" ")
    for word in words:
        if words[0] == "hello":
            return "$0"
        elif word[0] == "h":
            return "$20"
        else:
            return "$0"




if __name__ == "__main__":
    main()