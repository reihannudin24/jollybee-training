
def main():
    inpUser = input()
    inNum1, inNum2 = inpUser.split()

    total = int(inNum1) - int(inNum2)
    print(total)

if __name__ == '__main__':
    main()
