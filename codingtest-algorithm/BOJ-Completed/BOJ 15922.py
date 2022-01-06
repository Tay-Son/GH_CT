import sys
import heapq as hq

N_ = int(sys.stdin.readline())
lst_ = []
for _ in range(N_):
    A_, B_ = map(int, sys.stdin.readline().split())
    hq.heappush(lst_, (min(A_, B_), max(A_, B_)))

answer_ = 0
ptr_s = lst_[0][0]
ptr_e = lst_[0][1]
for S_, E_ in lst_[1:]:
    if S_ <= ptr_e:
        ptr_e = max(ptr_e, E_)
    else:
        answer_ += ptr_e - ptr_s
        ptr_s = S_
        ptr_e = E_
answer_ += ptr_e - ptr_s
print(answer_)

exit()