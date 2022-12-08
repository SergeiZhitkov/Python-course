def main():
    mass = int(input("Enter mass in kg: "))
    print(formula(mass))





def formula(m):
    return 1000 * m * pow(300000000, 2)




if __name__ == "__main__":
    main()