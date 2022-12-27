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
        return self.capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity != int(capacity) or capacity < 0:
            raise ValueError("Invalid input")
        self.capacity = capacity

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, size):
        if size != int(size) or size > self.capacity or < 0:
            raise ValueError("Invalid input")
        self.size = size

def main():
    try:
        self.capasity = input("Capasity of jar: ")
    except ValueError:

    try:
        self.deposit = input("Cookies: ")
    except ValueError:







if "__name__" == "__main__":
    main()