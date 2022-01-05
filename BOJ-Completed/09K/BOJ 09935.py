import sys


def func(mat_a, mat_b):
    mat_out = [[0 for _ in range(len(mat_b[0]))] for _ in range(len(mat_a[1]))]
    for idx_a in range(len(mat_out[0])):
        for idx_b in range(len(mat_out)):
            mat_out[idx_a][idx_b] = sum([mat_a[idx_a][i] * mat_b[i][idx_b] for i in range(len(mat_a[0]))])
            mat_out[idx_a][idx_b] %= 1000
    return mat_out


N, B = map(int, sys.stdin.readline().split())
mat_ = []
for _ in range(N):
    mat_.append(list(map(lambda x: int(x) % 1000, sys.stdin.readline().split())))


def func2(mat, b):
    if b == 1:
        return mat
    else:
        temp_ = func2(mat, b // 2)
        temp_ = func(temp_, temp_)
        if b % 2:
            temp_ = func(mat_, temp_)
        return temp_


answer_ = func2(mat_, B)

for each_ in answer_:
    print(' '.join(map(str, each_)))