import sys

INF_ = 10 ** 9

N_, K_ = map(int, sys.stdin.readline().split())
lst_ = []
for _ in range(N_):
    lst_.append(int(sys.stdin.readline()))

lst_dp = [0]
for idx_ in range(1, K_ + 1):
    min_ = INF_
    for each_ in lst_:
        temp_ = idx_ - each_
        if 0 <= temp_:
            min_ = min(min_, lst_dp[temp_])
    lst_dp.append(min_ + 1)

temp_ = lst_dp[-1]
if temp_ < INF_:
    print(temp_)
else:
    print(-1)

exit()