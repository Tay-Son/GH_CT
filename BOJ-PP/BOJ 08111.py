import sys

for _ in range(int(sys.stdin.readline())):
    N_ = int(sys.stdin.readline())
    if N_ == 1:
        print('1')
    else:
        lst_rem = [[-1, -1] for _ in range(N_ + 1)]

        is_ = False
        ptr_que = 0

        lst_rem[1 % N_] = [-1, 1]
        que_ = [1]

        while ptr_que < len(que_):
            curr_ = que_[ptr_que]

            for offset_ in range(2):
                rem_ = (curr_ * 10 + offset_) % N_
                if lst_rem[rem_][1] == -1:
                    lst_rem[rem_] = [curr_, offset_]
                    if rem_:
                        que_.append(rem_)
                    else:
                        is_ = True
                        break
            if is_:
                break
            else:
                ptr_que += 1

        if is_:
            lst_ = []
            while lst_rem[rem_][1] != -1:
                lst_.append(lst_rem[rem_][1])
                rem_ = lst_rem[rem_][0]
            print(''.join(map(str, reversed(lst_))))
        else:
            print('BRAK')
exit()
