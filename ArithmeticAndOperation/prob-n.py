
def main():
    inpNum = input()
    num1, num2 = inpNum.split()

    num1 = int(num1)
    num2 = int(num2)

    percentage = ((num1 - num2) / num1) * 100
    print(f"{percentage:.2f}%")

if __name__ == '__main__':
    main()
