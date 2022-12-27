class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.n = n
        self.size = self.size + n

    def withdraw(self, n):
        self.n = n
        self.size = self.size - n


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity != int(capacity) or capacity < 0:
            raise ValueError("Invalid input")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size != int(size) or size > self.capacity or size < 0:
            raise ValueError("Invalid input")
        self._size = size

def main():
    try:
        Jar.capacity = input("Capasity of jar: ")
    except ValueError:
        print("Kek")
    try:
        Jar.deposit = int(input("Add cookies: "))
    except ValueError:
        print("Kek")
    Jar.withdraw = int(input("Remove cookies: "))

    print(Jar)






if __name__ == "__main__":
    main()