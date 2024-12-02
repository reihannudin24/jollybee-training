def main():
    # Membaca jumlah kasus (selalu 3)
    T = int(input())

    # Iterasi untuk membaca dan menghitung setiap kasus
    for _ in range(T):
        P, N = map(int, input().split())
        # Hitung persentase
        result = (P / 100) * N
        # Cetak hasil dengan 2 angka di belakang koma
        print(f"{result:.2f}")


if __name__ == "__main__":
    main()
