import sys

N, K = map(int, sys.stdin.readline().split())
mod_ = 1000000007

p_ = 1
for cnt_ in range(1, min(K, N - K) + 1):
    p_ *= cnt_
    p_ %= mod_
p_c1 = p_

for cnt_ in range(min(K, N - K) + 1, max(K, N - K) + 1):
    p_ *= cnt_
    p_ %= mod_
p_c2 = p_

for cnt_ in range(max(K, N - K) + 1, N + 1):
    p_ *= cnt_
    p_ %= mod_
p_n = p_

print((p_n * pow(p_c1 * p_c2, mod_ - 2, mod_)) % mod_)
