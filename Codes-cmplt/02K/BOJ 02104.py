import sys

N_ = int(sys.stdin.readline())
lst_ = [-1] + list(map(int, sys.stdin.readline().split())) + [-1]

sum_ = 0
lst_sum = [0]
for each_ in lst_[1:N_ + 1]:
    sum_ += each_
    lst_sum.append(sum_)

stk_l = [0]
stk_r = [N_ + 1]
lst_answer = [[0, 0] for _ in range(N_ + 1)]

for idx_l in range(1, N_ + 1):
    idx_r = N_ - idx_l + 1

    while lst_[stk_l[-1]] >= lst_[idx_l]:
        stk_l.pop(-1)
    lst_answer[idx_l][0] = stk_l[-1]
    stk_l.append(idx_l)

    while lst_[stk_r[-1]] >= lst_[idx_r]:
        stk_r.pop(-1)
    lst_answer[idx_r][1] = stk_r[-1]
    stk_r.append(idx_r)

max_ = 0
for idx_ in range(1, N_ + 1):
    max_ = max(max_, lst_[idx_] * (lst_sum[lst_answer[idx_][1] - 1] - lst_sum[lst_answer[idx_][0]]))
print(max_)

exit()
