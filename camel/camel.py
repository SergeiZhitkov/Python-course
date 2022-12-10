def main():
    camel_case = input("Your message in camelCase: ")
    print(camel_to_snake(camel_case))




def camel_to_snake(c):
    s = ""
    for letter in c:
        if letter.isupper():
            s = s + "_" + letter.lower()
        else:
            s = s + letter
    return s




if __name__ == "__main__":
    main()