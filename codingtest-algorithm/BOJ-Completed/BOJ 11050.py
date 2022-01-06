import sys

N, K = map(int, sys.stdin.readline().split())

val_a = 1
val_b = 1
for cnt_ in range(1, min(K, N - K) + 1):
    val_a *= N - cnt_ + 1
    val_b *= cnt_
print(val_a // val_b)
