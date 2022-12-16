import sys
def main():
    word = input("Enter your message: ").strip()
    print(shorten(word))




def shorten(word):
    if word.isalpha():
        ov = ""
        for letter  in word:
            if letter not in "aeiouAEIOU":
                ov = ov + letter
        return ov
    else:
        raise("TypeError")
        sys.exit()



if __name__ == "__main__":
    main()