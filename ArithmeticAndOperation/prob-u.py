def main():
    T = int(input())  # Membaca jumlah kasus
    for _ in range(T):
        A, B = map(int, input().split())  # Membaca A dan B untuk setiap kasus
        total_degrees = A * B  # Menghitung total derajat yang diputar
        rotations = total_degrees / 360  # Menghitung jumlah rotasi
        print(f"{rotations:.2f}")  # Mencetak hasil dengan 2 angka di belakang koma

if __name__ == "__main__":
    main()
