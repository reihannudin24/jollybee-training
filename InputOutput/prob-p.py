def inOut():
    text = input("Name: ")  # Prompt the user and store input in text
    text = text.strip()  # Trim leading and trailing whitespace
    print(f"{text}-san.")  # Print the trimmed text followed by '-san'

def main():
    inOut()

if __name__ == '__main__':
    main()
