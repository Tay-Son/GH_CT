import sys

N_ = int(sys.stdin.readline())
lst_ = []
for _ in range(N_):
    lst_.append(list(map(int, sys.stdin.readline().split())))

lst_dp = [lst_[0]]

if N_ > 1:
    for cnt_ in range(1, N_):
        lst_dp.append([min(lst_dp[-1][1], lst_dp[-1][2]) + lst_[cnt_][0],
                       min(lst_dp[-1][0], lst_dp[-1][2]) + lst_[cnt_][1],
                       min(lst_dp[-1][0], lst_dp[-1][1]) + lst_[cnt_][2]])

print(min(lst_dp[-1]))

exit()
