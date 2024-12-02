def main():
    inpUser = input()
    inNum1, inNum2 = inpUser.split()
    inNum1 = int(inNum1)
    inNum2 = int(inNum2)

    add = inNum1 + inNum2
    sub = inNum1 - inNum2
    mul = inNum1 * inNum2
    div = inNum1 / inNum2
    mod = inNum1 % inNum2
    print(int(add))
    print(int(sub))
    print(int(mul))
    print(int(div))
    print(int(mod))


if __name__ == '__main__':
    main()
