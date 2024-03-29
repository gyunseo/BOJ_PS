import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def read_input():
    global N, M, 나무_높이들
    N, M = map(int, input().rstrip().split())
    나무_높이들 = [*map(int, input().rstrip().split())]


def get_parametric_search_res():
    lo = 0
    hi = 10**9 + 1

    def is_valid_height(mid):
        return sum(filter(lambda x: x > 0, map(lambda y: y - mid, 나무_높이들))) >= M

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if is_valid_height(mid):
            lo = mid
        else:
            hi = mid

    return lo


def solve():
    return get_parametric_search_res()


if __name__ == "__main__":
    read_input()
    print(solve())
