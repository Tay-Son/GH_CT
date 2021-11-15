import sys
from math import gcd

# tot_ = 1
# for num_ in range(1, 10):
#     tot_ *= num_
# print(tot_)

N_ = int(sys.stdin.readline())
lst_ = [sys.stdin.readline().strip() for _ in range(N_)]
K_ = int(sys.stdin.readline())

grd_dp = [[0 for _ in range(K_)] for _ in range(2 ** N_)]
grd_dp[0][0] = 1

lst_cch = [1 % K_]
for _ in range(50):
    lst_cch.append(lst_cch[-1] * 10 % K_)
print(lst_cch)

lst_cch_str = []
for str_ in lst_:
    lst_cch_str.append(int(str_) % K_)
print(lst_cch_str)

for curr_ in range(2 ** N_):
    for idx_n in range(N_):
        if not curr_ & (2 ** idx_n):
            next_s = curr_ | (2 ** idx_n)
            for idx_k in range(K_):
                next_k = ((idx_k * lst_cch[len(lst_[idx_n])]) % K_ + lst_cch_str[idx_n]) % K_
                grd_dp[next_s][next_k] += grd_dp[curr_][idx_k]

deno_ = 1
for num_ in range(1, N_ + 1):
    deno_ *= num_
nume_ = grd_dp[-1][0]
gcd_ = gcd(deno_, nume_)

print(nume_, deno_)
print(str(nume_ // gcd_) + '/' + str(deno_ // gcd_))

exit()
