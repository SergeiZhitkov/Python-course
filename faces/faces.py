def main():
    message = input()
    print(convert(message))






def convert(m):
    m = m.replace(":)","🙂")
    m = m.replace(":(", "🙁")
    return m




if __name__ == "__main__":
    main()