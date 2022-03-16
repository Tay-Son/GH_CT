import sys
from collections import deque

N_, K_ = map(int, sys.stdin.readline().split())

que_ = deque([(N_, N_)])
ran_ = max(N_, K_) * 2
lst_p = [-1 for _ in range(ran_)]

while que_:
    pos_, p_ = que_.popleft()
    print(pos_, p_)
    if lst_p[pos_] == -1:
        lst_p[pos_] = p_
        if pos_ == K_:
            cnt_ = 0
            lst_ = []
            while pos_ != N_:
                cnt_ += 1
                lst_.append(pos_)
                pos_ = lst_p[pos_]
            lst_.append(pos_)
            print(cnt_)
            print(' '.join(map(str, lst_[::-1])))
            break
        else:
            if pos_ - 1 >= 0:
                que_.append((pos_ - 1, pos_))
            if pos_ + 1 < ran_:
                que_.append((pos_ + 1, pos_))
            if pos_ * 2 < ran_:
                que_.append((pos_ * 2, pos_))

exit()
