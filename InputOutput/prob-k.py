def inOut():
    name = input("Name: ")
    nis_age = input("NIS and Age (format: NIS Age): ")

    nis, age = nis_age.split()

    print(f"Name: {name}")
    print(f"NIS: {nis}")
    print(f"Age: {age}")

def main():
    inOut()

if __name__ == '__main__':
    main()
