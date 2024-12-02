def main():
    inpNum = input()
    num1, num2 = inpNum.split()

    num1 = int(num1)
    num2 = int(num2)

    percentage = (num2 / num1) * 100

    print(f"{percentage:.4f}%")

if __name__ == '__main__':
    main()
