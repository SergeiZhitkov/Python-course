def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 1 < len(s) < 7:
        for letter in s[1:]:
            if letter.isalpha() and s[letter - 1].isalpha():
                continue
            elif letter.isnumeric():
                continue
            else:
                return False
        return True






if __name__ == "__main__":
    main()