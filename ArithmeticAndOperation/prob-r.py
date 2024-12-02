def main():
    results = []

    for _ in range(3):  # We need to process 3 lines of input
        inp = input().strip()  # Read the input line

        # Extracting numbers using the format (A + B)x(C - D)
        # Split based on `+`, `-`, and `x`
        parts = inp.split('x')
        first_part = parts[0].strip('()')
        second_part = parts[1].strip('()')

        # Now extract A, B from (A + B) and C, D from (C - D)
        A, B = map(int, first_part.split('+'))
        C, D = map(int, second_part.split('-'))

        # Compute the result (A + B) * (C - D)
        result = (A + B) * (C - D)

        # Append the result to the list
        results.append(result)

    # Print the results in one line, space-separated
    print(" ".join(map(str, results)))


if __name__ == '__main__':
    main()
