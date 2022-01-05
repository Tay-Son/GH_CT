import sys

for _ in range(int(sys.stdin.readline())):
    A_, B_ = map(int, sys.stdin.readline().split())
    lst_iv = [[-1, ''] for idx_ in range(10000)]
    lst_iv[A_] = [-2, '']

    ptr_que = 0
    que_ = [A_]
    while ptr_que < len(que_):
        curr_ = que_[ptr_que]

        if curr_ != B_:
            #
            target_ = (2 * curr_) % 10000
            if lst_iv[target_][0] == -1:
                lst_iv[target_] = [curr_, 'D']
                que_.append(target_)

            #
            if curr_ == 0:
                target_ = 9999
            else:
                target_ = curr_ - 1
            if lst_iv[target_][0] == -1:
                lst_iv[target_] = [curr_, 'S']
                que_.append(target_)

            #
            temp_, target_ = divmod(curr_, 1000)
            target_ = 10 * target_ + temp_
            if lst_iv[target_][0] == -1:
                lst_iv[target_] = [curr_, 'L']
                que_.append(target_)

            #
            target_, temp_ = divmod(curr_, 10)
            target_ = target_ + temp_ * 1000
            if lst_iv[target_][0] == -1:
                lst_iv[target_] = [curr_, 'R']
                que_.append(target_)

            ptr_que += 1
        else:
            break

    lst_ = []
    curr_ = B_
    while curr_ != A_:
        lst_.append(lst_iv[curr_][1])
        curr_ = lst_iv[curr_][0]
    print(''.join(reversed(lst_)))

exit()
