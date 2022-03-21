import sys

N_ = int(sys.stdin.readline())

lst_dp = [1]
for num_ in range(2, N_ + 2):
    lst_temp = [0 for _ in range(num_)]
    for idx_, val_ in enumerate(lst_dp):
        lst_temp[idx_] += val_
        lst_temp[idx_ + 1] += val_
    lst_dp = lst_temp
print(sum(lst_dp))
exit()
