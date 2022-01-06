import sys
import heapq as hq

INF_ = 1e9
data_max = 100000
S_, E_ = map(int, sys.stdin.readline().split())

lst_ = [INF_ for idx_ in range(data_max + 1)]
lst_[S_] = 0
que_ = [(0, S_)]

while que_:
    c_w, c_i = hq.heappop(que_)
    if c_w <= lst_[c_i]:
        temp_ = c_w + 1
        if c_i < data_max and temp_ < lst_[c_i + 1]:
            lst_[c_i + 1] = temp_
            hq.heappush(que_, (temp_, c_i + 1))
        if 0 < c_i and temp_ < lst_[c_i - 1]:
            lst_[c_i - 1] = temp_
            hq.heappush(que_, (temp_, c_i - 1))
        if c_i < (data_max // 2 + 1) and c_w < lst_[2 * c_i]:
            lst_[2 * c_i] = c_w
            hq.heappush(que_, (c_w, 2 * c_i))

print(lst_[E_])

exit()
