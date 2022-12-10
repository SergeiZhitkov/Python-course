import math
def main():
    cost = 50
    while True:
        if cost <= 0:
            print(f"Change Owed: {abs(cost)}")
            break
        print(f"Amount Due: {cost}")
        coin = int(input("Insert Coin: "))
        if check_coin(coin):
            cost = cost - coin



def check_coin(c):
    allowed_values = [5, 10, 25]
    if c in allowed_values:
        return True
    return False






if __name__ == "__main__":
    main()