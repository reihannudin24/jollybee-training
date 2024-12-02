def main():
    for _ in range(3):
        inpRow = input()
        a, b, c, d = map(int, inpRow.split())

        total = (a / 1 + b / 2 + c / 3 + d / 4) + (b / 2 + c / 3 + d / 4 + c / 3) + (c / 3 + d / 4 + c / 3 + b / 2) + (
                    d / 4 + c / 3 + b / 2 + a / 1)

        print(f"{total:.2f}")


if __name__ == '__main__':
    main()
