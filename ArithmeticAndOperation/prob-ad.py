

def main():
    Ph, M, Pu = map(int, input().split())
    final_score = (0.2 * Ph) + (0.3 * M) + (0.5 * Pu)
    print(f"{final_score:.2f}")

if __name__ == '__main__':
    main()
