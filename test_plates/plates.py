def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    if 1 < len(s) < 7:
        for letter in s:
            if letter.isalpha():
                i += 1
                continue
            elif letter.isnumeric() and letter != '0':
                i += 1
                for letter in s[i:]:
                    if letter.isnumeric():
                        i += 1
                        continue
                    else:
                        return False
                return True
            else:
                return False
        return True
    else:
        return False






if __name__ == "__main__":
    main()