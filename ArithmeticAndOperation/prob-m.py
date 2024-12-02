def main():
    # Input: dua angka X dan Y yang dipisahkan oleh spasi
    inpNum = input()
    num1, num2 = inpNum.split()

    num1 = int(num1)  # jumlah kartu Pokémon yang dimiliki Bibi
    num2 = int(num2)  # total jenis kartu Pokémon yang ada

    # Menghitung persentase kartu Pokémon yang dimiliki
    percentage = (num1 / num2) * 100

    # Output hasil dengan format 2 angka desimal dan simbol persen
    print(f"{percentage:.2f}%")

if __name__ == '__main__':
    main()
