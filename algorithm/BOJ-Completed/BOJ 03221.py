import sys

L_, T_ = map(int, sys.stdin.readline().split())
N_ = int(sys.stdin.readline())
lst_ = []
lst_idx = [idx_ for idx_ in range(N_)]
for _ in range(N_):
    pos_, dir_ = sys.stdin.readline().split()
    pos_ = int(pos_)
    if dir_ == 'L':
        pos_ = L_ + L_ - pos_
    lst_.append(pos_)

lst_idx = [idx_ for _, idx_ in zip(lst_, lst_idx)]

lst_answer = []
for pos_ in lst_:
    pos_ = (pos_ + T_) % (2 * L_)
    if pos_ > L_:
        pos_ = 2 * L_ - pos_
    lst_answer.append(pos_)

lst_answer.sort()
lst_answer = [pos_ for _, pos_ in zip(lst_idx, lst_answer)]

print(' '.join(map(str, lst_answer)))

exit()
