def main():
    inpNum = input()
    num1, num2 = inpNum.split()

    num1 = int(num1)  # jumlah uang
    num2 = float(num2)  # harga kartu

    total = num1 / num2

    print(f"{int(total)}")

if __name__ == '__main__':
    main()
