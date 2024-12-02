
def main():
    inNum = int(input())
    values = 100
    point = 0

    for bonusPoint in range(inNum):
        point += values + (50 * bonusPoint)

    print(point)

if __name__ == '__main__':
    main()
