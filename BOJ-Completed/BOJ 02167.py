import sys

N, M = map(int, sys.stdin.readline().split())
lst_input = list(map(int, sys.stdin.readline().split()))

lst_ = []
sum_ = 0
lst_temp = []
for idx_M in range(M):
    sum_ += lst_input[idx_M]
    lst_temp.append(sum_)
lst_.append(lst_temp)

if N > 1:
    for idx_N in range(1, N):
        lst_input = list(map(int, sys.stdin.readline().split()))
        lst_temp = []
        sum_ = 0
        for idx_M in range(M):
            sum_ += lst_input[idx_M]
            lst_temp.append(sum_ + lst_[-1][idx_M])
        lst_.append(lst_temp)

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    i, j, x, y = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    answer_ = lst_[x][y]
    if i != 0:
        answer_ -= lst_[i - 1][y]
    if j != 0:
        answer_ -= lst_[x][j - 1]
        if i != 0:
            answer_ += lst_[i - 1][j - 1]
    print(answer_)