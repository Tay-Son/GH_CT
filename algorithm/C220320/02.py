import sys

for T_ in range(1,int(sys.stdin.readline())+1):
    N_ = int(sys.stdin.readline())
    A_, B_ = map(int, sys.stdin.readline().split())
    lst_a = []
    lst_b = []
    for _ in range(N_):
        a_, b_ = map(int, sys.stdin.readline().split())
        lst_a.append(a_)
        lst_b.append(b_)

    print('Material Management '+str(T_))
    print('Classification ---- End!')

    #
    # lst_dp = [0 for _ in range(N_ + 1)]
    #
    # for idx_ in range(A_):
    #     lst_temp = []
    #     for idx_b in range(B_):
    #         if idx_b >= lst_b[idx_]:
    #             lst_temp.append(max(lst_b[idx_] + lst_dp[idx_b - lst_a[idx_]], lst_dp[idx_b]))
    #     lst_dp = lst_temp
    # print(lst_dp[-1])

exit()

import sys

N_, K_ = map(int, sys.stdin.readline().split())
lst_W = []
lst_V = []
for _ in range(N_):
    W_, V_ = map(int, sys.stdin.readline().split())
    lst_W.append(W_)
    lst_V.append(V_)

lst_dp = [0 for _ in range(K_ + 1)]

for idx_ in range(N_):
    lst_temp = []
    for idx_w in range(K_ + 1):
        if idx_w >= lst_W[idx_]:
            lst_temp.append(max(lst_V[idx_] + lst_dp[idx_w - lst_W[idx_]], lst_dp[idx_w]))
        else:
            lst_temp.append(lst_dp[idx_w])
    lst_dp = lst_temp
print(lst_dp[-1])
exit()
