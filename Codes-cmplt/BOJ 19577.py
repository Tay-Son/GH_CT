import sys

N_ = int(sys.stdin.readline())

if N_ < 2:
    print(N_)
elif N_ % 2:
    print(-1)
else:
    lst_ = [1, 2]
    for cnt_ in range(3, int(N_ ** .5) + 1):
        if not N_ % cnt_:
            lst_.append(cnt_)
    lst_temp = []
    for each_ in reversed(lst_):
        temp_ = N_ // each_
        if temp_ != each_:
            lst_temp.append(temp_)
    lst_ += lst_temp

    is_ = False
    for each_ in lst_:
        temp_ = each_
        answer_ = each_

        for sn_ in range(2, int(each_ ** .5) + 1):
            if not each_ % sn_:
                answer_ -= answer_ // sn_
                while not each_ % sn_:
                    each_ //= sn_
        if each_ > 1:
            answer_ -= answer_ // each_
        if answer_ * temp_ == N_:
            is_ = True
            break
    if is_:
        print(temp_)
    else:
        print(-1)
exit()
