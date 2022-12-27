class Jar:
    def __init__(self, capacity):
        self.capacity = capacity

    def __str__(self):
        return f"🍪 * {self.size}"

    def deposit(self, n):
        self.n = n
        self.size = self.size + n


    def withdraw(self, n):
        self.n = n
        self.size = self.size - n


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
        if size != int(size) or size > self.capacity or size < 0:
            raise ValueError("Invalid input")
        self.size = size

    @classmethod
    def get(cls):
        capacity = int(input("Capacity: "))
        return cls(capacity)

def main():
    jar = Jar.get()
    print(jar)





if __name__ == "__main__":
    main()