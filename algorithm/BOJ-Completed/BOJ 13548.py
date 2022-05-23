import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

M_ = int(sys.stdin.readline())
lst_q = []
for idx_ in range(M_):
    a_, b_ = map(int, sys.stdin.readline().split())
    a_ -= 1
    lst_q.append((a_, b_, idx_))

lst_q.sort(key=lambda x_: (x_[0] // (N_ ** .5)) * 1000000 + x_[1])
lst_ans = [0 for _ in range(M_)]

lst_val = [0 for _ in range(100001)]
lst_cnt = [0 for _ in range(100001)]
# lst_cnt[0] = 100000
max_ = 0
ptr_a = 0
ptr_b = 0

for a_, b_, idx_ in lst_q:
    while ptr_b < b_:
        val_b = lst_[ptr_b]
        lst_val[val_b] += 1
        cnt_ = lst_val[val_b]
        lst_cnt[cnt_ - 1] -= 1
        lst_cnt[cnt_] += 1
        if max_ == cnt_ - 1:
            max_ = cnt_
        ptr_b += 1

    while b_ < ptr_b:
        ptr_b -= 1
        val_b = lst_[ptr_b]
        lst_val[val_b] -= 1
        cnt_ = lst_val[val_b]
        lst_cnt[cnt_ + 1] -= 1
        lst_cnt[cnt_] += 1
        if max_ == cnt_ + 1 and not lst_cnt[cnt_ + 1]:
            max_ = cnt_

    while ptr_a < a_:
        val_a = lst_[ptr_a]
        lst_val[val_a] -= 1
        cnt_ = lst_val[val_a]
        lst_cnt[cnt_ + 1] -= 1
        lst_cnt[cnt_] += 1
        if max_ == cnt_ + 1 and not lst_cnt[cnt_ + 1]:
            max_ = cnt_
        ptr_a += 1

    while a_ < ptr_a:
        ptr_a -= 1
        val_a = lst_[ptr_a]
        lst_val[val_a] += 1
        cnt_ = lst_val[val_a]
        lst_cnt[cnt_ - 1] -= 1
        lst_cnt[cnt_] += 1
        if max_ == cnt_ - 1:
            max_ = cnt_

    # print(a_, b_, ptr_a, ptr_b, idx_, max_)
    lst_ans[idx_] = max_

for each_ in lst_ans:
    print(each_)
# print('\n'.join(map(str, lst_ans)))

exit()
