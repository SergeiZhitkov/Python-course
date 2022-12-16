def main():
    word = input("Enter your message: ").strip()
    print(shorten(word))




def shorten(word):
    ov = ""
    for letter  in word:
        if letter not in "aeiouAEIOU":
            ov = ov + letter
    return ov



if __name__ == "__main__":
    main()