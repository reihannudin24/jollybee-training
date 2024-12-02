

def main():
    T, Ut, Ua = map(int, input().split())
    final_score = (0.2 * T) + (0.3 * Ut) + (0.5 * Ua)
    print(f"{final_score:.2f}")

if __name__ == '__main__':
    main()
