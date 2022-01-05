import sys

N, M = map(int, sys.stdin.readline().split())
dct_n = {}
dct_i = {}
for idx_ in range(1, N + 1):
    str_input = sys.stdin.readline().split()[0]
    dct_n[idx_] = str_input
    dct_i[str_input] = idx_
for _ in range(M):
    str_input = sys.stdin.readline().split()[0]
    if 'A' <= str_input[0] <= 'Z':
        print(dct_i[str_input])
    else:
        print(dct_n[int(str_input)])