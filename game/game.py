import random



while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass


answer = random.rangint(1, leel)