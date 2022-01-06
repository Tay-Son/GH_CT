import sys
import time


lst_ = [[0, 1], [1, 0]]
lst_ = [0,1]
lst_dp = [-1.0 for _ in range(1001)]
def func_(N_):
    temp_ =lst_dp[N_]
    if lst_dp[N_] < 0:
        curr_ = len(lst_)
        while len(lst_) <= N_:
            fact_ = lst_[-1][0] * curr_
            not_ = 1
            for cnt_ in range(1, curr_):
                not_ += (fact_ // (lst_[curr_ - cnt_][0] * lst_[cnt_][0])) * lst_[cnt_][1]
            lst_.append([fact_, fact_ - not_])

            curr_ += 1



    else:
        return temp_




start_ = time.time()
for C_ in range(1,int(sys.stdin.readline())+1):
    N_ = int(sys.stdin.readline())
    lst_ = list(map(int,sys.stdin.readline().split()))
    cnt_ = 0
    for idx_ in range(1, N_+1):
        if lst_[idx_] != idx_:
            cnt_ += 1
    func_(cnt_)

    print('Case #'+C_+': '+func_(N_))
print(time.time()-start_)
exit()
