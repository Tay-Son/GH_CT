import sys
from collections import deque

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    N_, T_ = map(int, sys.stdin.readline().split())
    lst_ = list(map(int, sys.stdin.readline().split()))
    lst_p = sorted(lst_)
    deq_ = deque(list(zip(lst_, range(N_))))

    cnt_ = 1
    while True:
        temp_ = deq_.popleft()
        if temp_[0] == lst_p[-1]:
            lst_p.pop()
            if temp_[1] == T_:
                break
            cnt_ += 1
        else:
            deq_.append(temp_)

    print(cnt_)

exit()