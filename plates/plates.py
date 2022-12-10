def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    if 1 < len(s) < 7:
        for letter in s[1:]:
            if letter.isalpha() and s[i].isalpha():
                i += 1
                continue
            elif letter.isnumeric():
                i += 1
                continue
            else:
                return False
            return True
        






if __name__ == "__main__":
    main()