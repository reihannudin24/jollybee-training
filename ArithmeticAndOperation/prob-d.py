def main():
    inpUser = input()
    inNum1, inNum2 = inpUser.split()
    inNum1 = int(inNum1)
    inNum2 = int(inNum2)

    total = inNum1

    for i in range(inNum2):
        total += 1
        print(total)

if __name__ == '__main__':
    main()
