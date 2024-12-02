
def oct_oct():
    decimal_number = int(input("Input (decimal): "))
    octdecimal = oct(decimal_number)[2:]
    print(f"{octdecimal}")

def main():
    oct_oct()


if __name__ == '__main__':
    main()
