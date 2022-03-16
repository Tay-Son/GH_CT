from itertools import permutations as pm

N, M = map(int, input().split())

for pm_ in pm(range(1, N + 1), M):
    print(' '.join(map(str, pm_)))