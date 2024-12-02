
def inOut():
    text = input("Text : ")
    words = text.split()
    reversed_text =  " ".join(reversed(words))
    print(f"Reversed Text: {reversed_text}")

def main():
    inOut()


if __name__ == '__main__':
    main()
