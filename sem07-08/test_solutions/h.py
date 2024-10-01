import sys
import typing as tp


def find_lost(*args: tp.Any) -> int:
    n = len(args) + 1
    sm = n * (n + 1) // 2
    return sm - sum(args)


# def find_lost(*args: tp.Any) -> int:
#     for i in range(1, len(args) + 2):
#         if i not in args:
#             return i


exec(sys.stdin.read())
