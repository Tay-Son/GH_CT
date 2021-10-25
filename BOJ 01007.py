import sys

INF_ = 30000000.0


def rec_(depth_, tot_, min_, lst_, lst_iv):
    if depth_ < len(lst_):
        ptr_a = 0
        while lst_iv[ptr_a]:
            ptr_a += 1
        lst_iv[ptr_a] = True

        depth_ += 2

        for offset_ in range(1, len(lst_) - depth_+3):
            ptr_b = ptr_a +1
            cnt_ = 1


            while lst_iv[ptr_b] or cnt_ < offset_:
                if not lst_iv[ptr_b]:
                    cnt_ += 1
                ptr_b += 1
            lst_iv[ptr_b] = True


            val_temp = tot_ + (lst_[ptr_a][0] - lst_[ptr_b][0]) ** 2 + (lst_[ptr_a][1] - lst_[ptr_b][1]) ** 2

            # if val_temp < min_:
            #     min_ = min(min_,rec_(depth_, val_temp, min_, lst_, lst_iv))

            min_ = min(min_,rec_(depth_, val_temp, min_, lst_, lst_iv))

            lst_iv[ptr_b] = False

        lst_iv[ptr_a] = False
        return min_

    else:
        print(tot_)
        return tot_


for _ in range(int(sys.stdin.readline())):
    lst_ = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]

    lst_.sort(key=lambda x: x[1])
    lst_.sort(key=lambda x: x[0])

    lst_iv = [False for _ in range(len(lst_))]

    print(rec_(1, 0.0, INF_, lst_, lst_iv))
    # print(rec_(1, 0.0, INF_, lst_, lst_iv) ** .5)

exit()
