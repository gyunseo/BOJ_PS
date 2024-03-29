import sys

# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

N, M = None, None
상근_카드 = [False for _ in range(2 * (10**7) + 1)]
숫자들 = None


def get_상근_카드_index(i):
    return i + 10**7


def read_input():
    global N, M, 상근_카드, 숫자들
    N = int(input().rstrip())
    for 카드 in input().rstrip().split():
        상근_카드[get_상근_카드_index(int(카드))] = True

    M = int(input().rstrip())
    숫자들 = [*map(int, input().rstrip().split())]


def solve():

    for 숫자 in 숫자들:
        if 상근_카드[get_상근_카드_index(숫자)]:
            print("1", end=" ")
        else:
            print("0", end=" ")


if __name__ == "__main__":
    read_input()
    solve()
