def main():
    inpNum = input()  # Input example: 1234 + 9999
    num1, operator, num2 = inpNum.split()  # Split input into components

    num1 = int(num1)
    num2 = int(num2)

    if operator == '+':
        total = num1 + num2
    elif operator == '-':
        total = num1 - num2
    elif operator == '*':
        total = num1 * num2
    elif operator == '/':
        total = num1 / num2
    else:
        total = None  # Invalid operator, though we assume input is valid as per the problem

    print(f"{total}")  # Print the result

if __name__ == '__main__':
    main()
