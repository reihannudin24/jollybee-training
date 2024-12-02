def main():
    # Membaca jumlah suhu yang akan dikonversi
    T = int(input())  # Dapat dipastikan T selalu 3 berdasarkan soal

    # Proses untuk setiap suhu yang diberikan
    for _ in range(T):
        # Membaca suhu dalam Celcius
        A = int(input())

        # Konversi suhu ke Reaumur, Fahrenheit, dan Kelvin
        R = A * 4 / 5
        F = A * 9 / 5 + 32
        K = A + 273.15

        # Menampilkan hasil konversi dengan format 2 angka di belakang koma
        print(f"{R:.2f} {F:.2f} {K:.2f}")


if __name__ == "__main__":
    main()
