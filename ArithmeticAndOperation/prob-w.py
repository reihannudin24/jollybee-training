def main():
    result = 0
    # Loop untuk membaca 3 angka
    for _ in range(3):
        n = int(input())

        # Mengambil digit tengah (puluhan)
        middle_digit = (n // 10) % 10
        print(middle_digit)

        # Menambahkan digit tengah ke hasil
        result += middle_digit

    # Outputkan hasil
    print(result)


if __name__ == "__main__":
    main()
