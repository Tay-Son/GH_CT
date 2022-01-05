import sys
import heapq as hq

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    k = int(sys.stdin.readline())
    que_min = []
    que_max = []
    idx_ = 0
    len_ = 0
    set_popped = set()
    for _ in range(k):
        lst_com = sys.stdin.readline().split()
        if lst_com[0] == 'I':
            val_ = int(lst_com[1])
            hq.heappush(que_min, (val_, val_, idx_))
            hq.heappush(que_max, (-val_, val_, idx_))
            idx_ += 1
            len_ += 1

        elif len_ > 0:
            if int(lst_com[1]) == 1:
                temp_ = hq.heappop(que_max)
                while temp_[2] in set_popped:
                    temp_ = hq.heappop(que_max)
                set_popped.add(temp_[2])
                len_ -= 1
            else:
                temp_ = hq.heappop(que_min)
                while temp_[2] in set_popped:
                    temp_ = temp_ = hq.heappop(que_min)
                set_popped.add(temp_[2])
                len_ -= 1

    if len_ > 0:
        temp_ = hq.heappop(que_max)
        while temp_[2] in set_popped:
            temp_ = hq.heappop(que_max)
        print(temp_[1], end=' ')

        temp_ = hq.heappop(que_min)
        while temp_[2] in set_popped:
            temp_ = hq.heappop(que_min)
        print(temp_[1])

    else:
        print('EMPTY')