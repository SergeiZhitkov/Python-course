class Test:
    def __init__(self, test_value=10):
        self.test_value = test_value


    def __str__(self):
        return f"{self.test_value}"

def main():
    test = Test()
    print(test)




if __name__ == "__main__":
    main()