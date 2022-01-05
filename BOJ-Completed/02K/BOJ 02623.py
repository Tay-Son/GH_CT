import sys
from collections import deque

N_, M_ = map(int, sys.stdin.readline().split())

grp_ = [[] for _ in range(N_ + 1)]
lst_visit_cntr = [0 for _ in range(N_ + 1)]

for _ in range(M_):
    lst_input = list(map(int, sys.stdin.readline().split()))
    for idx_ in range(1, len(lst_input) - 1):
        idx_subject = lst_input[idx_]
        idx_target = lst_input[idx_ + 1]
        grp_[idx_subject].append(idx_target)
        lst_visit_cntr[idx_target] += 1

deq_ = deque()
for idx_ in range(1, N_ + 1):
    if not lst_visit_cntr[idx_]:
        deq_.append(idx_)

lst_ans = []
while deq_:
    curr_ = deq_.popleft()
    lst_ans.append(curr_)
    for each_ in grp_[curr_]:
        lst_visit_cntr[each_] -= 1
        if not lst_visit_cntr[each_]:
            deq_.append(each_)

if len(lst_ans) == N_:
    print('\n'.join(map(str, lst_ans)))
else:
    print(0)

exit()
