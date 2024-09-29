from collections import defaultdict


def main():
    n, m = (int(e) for e in input().split())
    users = set()
    orders = defaultdict(set)
    for _ in range(n):
        user, order = input().split()
        orders[order].add(user)
        users.add(user)
    for _ in range(m):
        order = input()
        print(len(users) - len(orders[order]))


if __name__ == "__main__":
    main()
