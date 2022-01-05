import sys

N_ = int(sys.stdin.readline())
grp_ = [[] for _ in range(N_ + 1)]
lst_ = [0]
lst_answer = [-1 for _ in range(N_ + 1)]
for idx_ in range(1, N_ + 1):
    lst_input = list(map(int, sys.stdin.readline().split()))
    lst_.append(lst_input[0])
    if len(lst_input) > 2:
        for idx_sub in range(2, len(lst_input)):
            grp_[lst_input[idx_sub]].append(idx_)


def func(idx_):
    if lst_answer[idx_] == -1:
        max_ = 0
        for each_ in grp_[idx_]:
            max_ = max(max_, func(each_))
        lst_answer[idx_] = max_ + lst_[idx_]
    return lst_answer[idx_]


for idx_ in range(1, N_ + 1):
    func(idx_)

print(max(lst_answer))

exit()