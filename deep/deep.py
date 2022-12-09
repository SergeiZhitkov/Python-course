def main():
    answer = input("What is the Answer to the Great Question of Life, The Universe and Everything? ").strip().lower()
    print(is_right(answer))



def is_right(a):
    if a == "42" or a == "forty-two" or a == "forty two":
        return "Yes"
    else:
        return "No"






if __name__ == "__main__":
    main()