import sys

lst_gear = [sys.stdin.readline().rstrip() for _ in range(4)]
K_ = int(sys.stdin.readline())
lst_state = [0, 0, 0, 0]
for _ in range(K_):
    num_, dir_ = map(int, sys.stdin.readline().split())
    num_ -= 1
    lst_o = [0, 0, 0, 0]
    lst_o[num_] = -dir_

    c_ = dir_
    for idx_ in range(num_ + 1, 4):
        if lst_gear[idx_ - 1][(2 + lst_state[idx_ - 1]) % 8] != lst_gear[idx_][(6 + lst_state[idx_]) % 8]:
            lst_o[idx_] = c_
            c_ *= -1
        else:
            break

    c_ = dir_
    for idx_ in range(num_ - 1, -1, -1):
        if lst_gear[idx_][(2 + lst_state[idx_]) % 8] != lst_gear[idx_ + 1][(6 + lst_state[idx_ + 1]) % 8]:
            lst_o[idx_] = c_
            c_ *= -1
        else:
            break

    print(lst_o)

    for idx_ in range(4):
        lst_state[idx_] += lst_o[idx_]

tot_ = 0
mag_ = 1
for idx_ in range(4):
    # print((-lst_state[idx_]) % 8)
    if lst_gear[idx_][(lst_state[idx_]) % 8] == '1':
        tot_ += mag_
    mag_ *= 2
print(tot_)

exit()
