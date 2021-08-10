import sys

N = int(sys.stdin.readline())
col, diag1, diag2 = set(), set(), set()


def dfs(y):
    if y == N:
        return 1
    else:
        tot_ = 0
        for x in range(N):
            if x in col or (x + y) in diag1 or (x - y) in diag2:
                continue
            col.add(x)
            diag1.add(x + y)
            diag2.add(x - y)
            tot_ += dfs(y + 1)
            col.remove(x)
            diag1.remove(x + y)
            diag2.remove(x - y)
        return tot_


print(dfs(0))