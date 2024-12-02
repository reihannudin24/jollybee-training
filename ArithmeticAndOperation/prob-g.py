def main():
    inpUser = input()

    char1, char2 = inpUser.split()

    ascii1 = ord(char1)
    ascii2 = ord(char2)

    product = ascii1 * ascii2

    print(product)

if __name__ == '__main__':
    main()
