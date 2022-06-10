import sys
from collections import deque

str_w = sys.stdin.readline().strip()
str_wr = str_w[::-1]
deq_ = deque(sys.stdin.readline().strip())

lst_l = []
lst_r = []
cnt_ = 0

while len(str_w) <= len(deq_):

    que_temp = deque()
    is_run_sub = True
    while is_run_sub and (len(str_w) <= len(deq_) + len(que_temp)):

        que_ = deque()
        str_t = str_w if not cnt_ % 2 else str_wr
        for each_chr in str_t:
            if que_temp:
                val_ = que_temp.popleft()
            else:
                if not cnt_ % 2:
                    val_ = deq_.popleft()
                else:
                    val_ = deq_.pop()
            que_.append(val_)

            if not val_ == each_chr:
                if not cnt_ % 2:
                    lst_l.append(que_.popleft())
                else:
                    lst_r.append(que_.popleft())
                break
        else:
            is_run_sub = False
            cnt_ += 1
    print(lst_l)
    print(list(deq_))
    print(lst_r[::-1])
    print(cnt_)
    print()

print(lst_l)
print(lst_r)
print(cnt_)
print(''.join(lst_l) + ''.join(deq_) + ''.join(lst_r[::-1]))

exit()
