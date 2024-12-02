
def main():
    inpNum = input()
    num1, num2 = inpNum.split()

    num1 = int(num1)
    num2 = int(num2)

    total = num1 * num2
    print(f"{total}")

if __name__ == '__main__':
    main()
