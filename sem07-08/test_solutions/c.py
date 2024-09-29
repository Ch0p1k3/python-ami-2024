import sys


def optimal_taxi(distance: list[int], price: list[int]) -> int:
    sorted_price = sorted(price)
    return sum(
        e * sorted_price[i]
        for i, e in enumerate(sorted(distance, reverse=True))
    )


exec(sys.stdin.read())
