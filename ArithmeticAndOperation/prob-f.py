def main():
    inpUser = input()

    inNum1, operator, inNum2, equalSign = inpUser.split()

    inNum1 = int(inNum1)
    inNum2 = int(inNum2)

    add = inNum1 + inNum2
    print(f"{inNum1} + {inNum2} = {add}")


if __name__ == '__main__':
    main()
