import sys
def main():
    word = input("Enter your message: ").strip()
    print(shorten(word))




def shorten(word):
    if word.is_alpha():
        ov = ""
        for letter  in word:
            if letter not in "aeiouAEIOU":
                ov = ov + letter
        return ov
    else:
        sys.exit()



if __name__ == "__main__":
    main()