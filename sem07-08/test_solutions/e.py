def main():
    n = int(input())
    pts = set()
    for _ in range(n):
        pts.add(input().split()[0])
    print(len(pts))


# 0 1   input() -> "0 1", .split() -> ["0", "1"], [0] -> "0"
# 0 2

if __name__ == "__main__":
    main()
