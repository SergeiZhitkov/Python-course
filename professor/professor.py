import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x, y = generate_integer(level)
        for i in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                pass
            if i == 2:
                print(f"{x} + {y} = {x+y}")
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return (random.randint(0, 9), random.randint(0, 9))
    elif level == 2:
        return (random.randint(10, 99), random.randint(10, 99))
    elif level == 3:
        return (random.randint(100, 999), random.randint(100, 999))
    raise ValueError


if __name__ == "__main__":
    main()