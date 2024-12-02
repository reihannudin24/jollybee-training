def main():
    # Jumlah baris input
    T = 3  # Selalu 3, sesuai deskripsi soal

    # Inisialisasi list untuk menyimpan hasil
    results = []

    # Loop sebanyak T baris
    for _ in range(T):
        # Input nilai a, b, c, d
        a, b, c, d = map(int, input().split())

        # Hitung total sum dari diamond
        total_sum = 2 * a + 4 * b + 6 * c + 4 * d

        # Hitung rata-rata dengan membagi 16
        result = total_sum / 8

        # Simpan hasil dengan format 2 angka desimal
        results.append(f"{result:.2f}")

    # Tampilkan hasil
    for res in results:
        print(res)


if __name__ == "__main__":
    main()
