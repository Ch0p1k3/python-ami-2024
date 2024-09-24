def main():
    n = int(input())
    if n == 0:
        print(10)
        return
    if n == 1:
        print(11)
        return
    result: list[str] = []
    for i in range(9, 1, -1):
        while n % i == 0 and n != 1:
            n //= i
            result.append(str(i))
    if len(result) == 0:
        print("No solution")
        return
    if len(result) == 1:
        result.append("1")
    print("".join(result[::-1]))


if __name__ == "__main__":
    main()
