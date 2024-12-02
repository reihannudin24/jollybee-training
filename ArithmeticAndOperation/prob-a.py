

def main():
    inInt = input("Number : ")
    num1, num2 = inInt.split()
    total = int(num1) + int(num2)
    print(f"Total : {total}")


if __name__ == '__main__':
    main()