def convert_time(time_str):
    # Fungsi untuk mengonversi waktu dari GMT+8 ke GMT+7
    start, end = time_str.split('-')

    # Fungsi untuk mengurangi satu jam dari waktu
    def subtract_one_hour(time):
        hour, minute = map(int, time.split(':'))
        hour -= 1
        if hour < 0:
            hour += 24  # Jika jam menjadi negatif, tambahkan 24
        return f"{hour:02}:{minute:02}"

    # Mengonversi waktu mulai dan waktu selesai
    start_converted = subtract_one_hour(start)
    end_converted = subtract_one_hour(end)

    return f"{start_converted}-{end_converted}"


def main():
    # Membaca input 5 baris
    for _ in range(5):
        # Input format: Course code HH:MM-HH:MM
        inp = input()

        # Memisahkan Course code dan waktu
        course_code, time_str = inp.split(' ', 1)

        # Mengonversi waktu
        converted_time = convert_time(time_str)

        # Menampilkan output dengan format yang benar
        print(f"{course_code} {converted_time}")


if __name__ == "__main__":
    main()
