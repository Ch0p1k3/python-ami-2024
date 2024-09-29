def main():
    n = int(input())
    pts = set()
    for _ in range(n):
        pts.add(input().split()[0])
    print(len(pts))


if __name__ == "__main__":
    main()
