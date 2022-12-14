import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x, y = generate_integer(level)
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
    if level < 1 or level > 3:
        raise ValueError
    if level == 1:
        return (random.randint(1, 9), random.randint(1, 9))
    elif level == 2:
        return (random.randint(1, 99), random.randint(1, 99))
    elif level == 3:
        return (random.randint(1, 999), random.randint(1, 999))



if __name__ == "__main__":
    main()