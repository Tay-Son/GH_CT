import sys
import heapq as hq

N_ = int(sys.stdin.readline())
lst_ = []
for _ in range(N_):
    A_, B_ = map(int, sys.stdin.readline().split())
    hq.heappush(lst_, (min(A_, B_), max(A_, B_)))

answer_ = 0
ptr_s, ptr_e = hq.heappop(lst_)
for _ in range(1, N_):
    S_, E_ = hq.heappop(lst_)
    if S_ <= ptr_e:
        ptr_e = max(ptr_e, E_)
    else:
        answer_ += ptr_e - ptr_s
        ptr_s = S_
        ptr_e = E_
answer_ += ptr_e - ptr_s
print(answer_)

exit()