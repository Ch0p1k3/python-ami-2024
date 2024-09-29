def main():
    arr = [int(e) for e in input().split() if int(e) % 2 == 0]
    print(*reversed(arr))


if __name__ == "__main__":
    main()
