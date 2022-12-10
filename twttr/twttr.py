def main():
    message = input("Enter your message: ").strip()
    print(omitting_vowels(message))




def omitting_vowels(m):
    ov = ""
    for letter  in m:
        if letter not in "aeiouAEIOU":
            ov = ov + letter
    return ov




if __name__ == "__main__":
    main()