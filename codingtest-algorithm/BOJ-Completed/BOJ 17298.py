import sys

N_ = int(sys.stdin.readline())
lst_input = list(map(int, sys.stdin.readline().split()))
lst_output = [-1 for _ in range(N_)]
stk_ = []

for idx_ in range(N_ - 1, -1, -1):
    curr_ = lst_input[idx_]
    while stk_ and stk_[-1] <= curr_:
        stk_.pop()
    if stk_:
        lst_output[idx_] = stk_[-1]

    stk_.append(curr_)

print(' '.join((map(str, lst_output))))
exit()

