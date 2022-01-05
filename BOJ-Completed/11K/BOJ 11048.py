import sys

val_n, val_m = map(int, sys.stdin.readline().split())
lst_ = []
for _ in range(val_n):
    lst_.append(list(map(int, sys.stdin.readline().split())))

lst_max = [[]]
for idx_m in range(val_m):
    lst_max[0].append(sum(lst_[0][:idx_m + 1]))

for idx_n in range(1, val_n):
    lst_temp = [lst_max[idx_n - 1][0] + lst_[idx_n][0]]
    for idx_m in range(1, val_m):
        val_a = lst_temp[-1]
        val_b = lst_max[idx_n - 1][idx_m]
        lst_temp.append(max(val_a, val_b) + lst_[idx_n][idx_m])
    lst_max.append(lst_temp)

print(lst_max[-1][-1])