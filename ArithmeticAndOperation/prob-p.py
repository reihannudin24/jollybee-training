def main():
    # Process 4 items
    for _ in range(4):
        N, P = map(int, input().split())  # Read N and P

        # Calculate the original price
        original_price = P / (1 - N / 100)

        # Print the result rounded to 2 decimal places with '$'
        print(f"${original_price:.2f}")

if __name__ == '__main__':
    main()
