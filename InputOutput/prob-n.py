def inOut():
    inputUser = input("Sample Input: ")

    data = inputUser.split()

    for i in range(0, len(data), 3):
        name = data[i]
        height = data[i + 1]
        age = data[i + 2]

        print(f"Name {i // 3 + 1}: {name}")
        print(f"Height {i // 3 + 1}: {height}")
        print(f"Age {i // 3 + 1}: {age}")


def main():
    inOut()


if __name__ == '__main__':
    main()
