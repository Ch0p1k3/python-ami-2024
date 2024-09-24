def main():
    n, m = (int(e) for e in input().split())
    d: dict[str, int] = {}
    for i in range(m):
        num, word = input().split()
        d[word] = int(num)
    results: list[int] = [0] * n
    for num in d.values():
        results[num - 1] += 1
    print(*results)


if __name__ == "__main__":
    main()
