
def inOut():
    text_id = input("ID : ")
    text_name = input("Name : ")
    text_class_and_num = input("Class & Num : ")
    text_class, text_num = text_class_and_num.split()

    print(f"Id : {text_id}")
    print(f"Name : {text_name}")
    print(f"Class : {text_class}")
    print(f"Num : {text_num}")


def main():
    inOut()


if __name__ == '__main__':
    main()
