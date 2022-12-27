class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.n = n
        if self.size + self.n > capacity:
            raise ValueError("Invalid input")
        self.size = self.size + n

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self.capasity

    @capasity.setter
    def capacity(self, capasity):
        if capacity != int(capasity) or capasity < 0:
            raise ValueError("Invalid input")
        self.capasity = capasity

    @property
    def size(self):
        return self.size

def main():
    try:
        self.capasity = input("Capasity of jar: ")
    except ValueError:

    try:
        self.deposit = input("Cookies: ")
    except ValueError:







if "__name__" == "__main__":
    main()