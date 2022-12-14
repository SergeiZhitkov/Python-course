import random


def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass

def generate_integer(level):
    score = 0
    if level < 1 or level > 3:
        raise ValueError
    if level == 1:
        for _ in range(10):
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            for _ in range(3):
                try:
                    answer = int(input(f"{x} + {y} = "))
                except ValueError:
                    print("EEE")
                    pass
                if answer == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                print(f"{x} + {y} = {x+y}")





if __name__ == "__main__":
    main()