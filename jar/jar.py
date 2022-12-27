class Jar:
    def __init__(self, capasity, deposit, withdraw):
        if capasity != int(capasity) or capasity < 0:
            raise ValueError("Invalid input")
        if deposit != int(deposit) or capasity < deposit or deposit < 0:
            raise ValueError("Invalid input")
        if withdraw != int(withdraw) or withdraw > deposit or withdraw < 0:
            raise ValueError("Invalid input")
        self.capasity = capasity
        self.deposit = deposit
        self.withdraw = withdraw


    def __str__(self):
        return "🍪" * self.deposit

def main():
    try:
        self.capasity = input("Capasity of jar: ")
    except ValueError:

    try:
        self.deposit = input("Cookies: ")
    except ValueError:







if "__name__" == "__main__":
    main()