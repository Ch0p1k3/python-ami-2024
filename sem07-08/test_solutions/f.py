from collections import defaultdict


def main():
    n = int(input())
    surnames = set()
    logins = defaultdict(int)
    for _ in range(n):
        surname, name = input().split()
        if surname not in surnames:
            surnames.add(surname)
            print(surname)
            continue
        login = f"{surname}_{name}"
        print(login + ("" if logins[login] == 0 else f"_{logins[login]}"))
        logins[login] += 1


if __name__ == "__main__":
    main()
