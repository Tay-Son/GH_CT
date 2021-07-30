import sys

N_ = int(sys.stdin.readline())

for cnt_ in range(N_):
    temp_ = cnt_
    answer_ = cnt_

    for sn_ in range(2, int(cnt_ ** .5) + 1):
        if not cnt_ % sn_:
            answer_ -= answer_ // sn_
            while not cnt_ % sn_:
                cnt_ //= sn_
    if cnt_ > 1:
        answer_ -= answer_ // cnt_
    print(temp_,answer_)

exit()

ptr_s = 0
ptr_e = 10 ** 9 + 1

while ptr_s < ptr_e:
    ptr_c = (ptr_s+ptr_e)

    answer_ = ptr_c

    for sn_ in range(2, int(ptr_c ** .5) + 1):
        if not ptr_c % sn_:
            answer_ -= answer_ // sn_
            while not ptr_c % sn_:
                ptr_c //= sn_
    if ptr_c > 1:
        answer_ -= answer_ // ptr_c

    if ptr_c * answer_ <= N_:
        ptr_e = ptr_c
    else:
        ptr_s = ptr_c + 1

if ptr_c * answer_ == N_:
    print(ptr_c)
else:
    print(-1)


exit()