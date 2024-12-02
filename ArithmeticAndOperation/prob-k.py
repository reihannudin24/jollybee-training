def main():
    # Input: jumlah uang dan bunga per bulan
    inpNum = input()
    num1, num2 = inpNum.split()

    num1 = int(num1)  # jumlah uang awal
    num2 = float(num2)  # persentase bunga per bulan

    # Rumus bunga majemuk untuk 3 bulan
    total = num1 * (1 + num2 / 100) ** 3

    # Output hasil dengan 2 angka desimal
    print(f"{total:.2f}")

if __name__ == '__main__':
    main()
