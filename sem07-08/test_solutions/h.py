import sys
import typing as tp


def find_lost(*args: tp.Any) -> int:
    n = len(args) + 1
    sm = n * (n + 1) // 2
    return sm - sum(args)


exec(sys.stdin.read())
