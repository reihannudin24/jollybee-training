
def loop_late_night_counting(start, count):
    for i in range(count):
        print(start + i)

def main():
    print("Sample 1")
    loop_late_night_counting(1 , 5)

    print("Sample 2")
    loop_late_night_counting(6, 5)

    print("Sample 3")
    loop_late_night_counting(10 , 10)

if __name__ == '__main__':
    main()