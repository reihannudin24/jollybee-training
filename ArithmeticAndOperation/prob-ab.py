
def main():
    inNum = int(input())
    baseDamage = 100
    totalDamage = 0

    for i in range(inNum):
        totalDamage += baseDamage + (50 * i)

    print(totalDamage)

if __name__ == '__main__':
    main()
