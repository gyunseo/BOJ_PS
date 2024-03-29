import sys

sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M, R = (None,) * 3
is_visited = [False for _ in range(100_000 + 1)]
adjacent_lists = [[] for _ in range(100_000 + 1)]


def read_input():
    global N, M, R
    N, M, R = map(int, input().rstrip().split())
    for _ in range(M):
        u, v = map(int, input().rstrip().split())
        adjacent_lists[u].append(v)
        adjacent_lists[v].append(u)


def sort_adjacent_lists():
    for adjacent_list in adjacent_lists:
        adjacent_list.sort()


def solution():
    visit_order = []
    ans = [0 for _ in range(N + 1)]

    def dfs(root):
        is_visited[root] = True
        visit_order.append(root)
        for nv in adjacent_lists[root]:
            if is_visited[nv]:
                continue
            dfs(nv)

    sort_adjacent_lists()
    dfs(R)
    for i in range(len(visit_order)):
        ans[visit_order[i]] = i + 1

    return "\n".join(map(str, ans[1:]))


if __name__ == "__main__":
    read_input()
    print(solution())
