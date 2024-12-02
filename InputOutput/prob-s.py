def inOut():
    text = input("Text: ")  # Get user input
    template = f'''
#include <stdio.h>
int main() {{
printf("%s\\n","{text}");
return 0;
}}
    '''
    print(template)  # Print the formatted template with the user's input

def main():
    inOut()

if __name__ == '__main__':
    main()
