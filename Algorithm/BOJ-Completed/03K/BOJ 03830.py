import sys

sys.setrecursionlimit(10 ** 5)


def find(idx_):
    temp_ = lst_g[idx_]
    if temp_[0] != idx_:
        temp_ = find(temp_[0])
        lst_g[idx_][0] = temp_[0]
        lst_g[idx_][1] += temp_[1]
    return lst_g[idx_]


def union(idx_a, idx_b, d_):
    p_a = find(idx_a)
    p_b = find(idx_b)

    p_d = p_a[1] + d_ - p_b[1]
    if p_d > 0:
        lst_g[p_a[0]][1] = -p_d
        lst_g[p_a[0]][0] = p_b[0]
    else:
        lst_g[p_b[0]][1] = p_d
        lst_g[p_b[0]][0] = p_a[0]


N_, M_ = list(map(int, sys.stdin.readline().split()))
while N_ != 0:
    lst_g = [[i_, 0] for i_ in range(N_ + 1)]

    for _ in range(M_):
        lst_input = sys.stdin.readline().split()
        if lst_input[0] == '!':
            union(int(lst_input[1]), int(lst_input[2]), int(lst_input[3]))
        else:
            temp_a = find(int(lst_input[1]))
            temp_b = find(int(lst_input[2]))
            if temp_a[0] == temp_b[0]:
                print(temp_b[1] - temp_a[1])
            else:
                print('UNKNOWN')
    N_, M_ = list(map(int, sys.stdin.readline().split()))

exit()
