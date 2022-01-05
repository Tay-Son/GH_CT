import sys

n, m = map(int, sys.stdin.readline().split())
val_a = 1
val_b = 1
c = 1
for cnt in range(min(m, n - m)):
    val_a *= n
    val_b *= c
    n -= 1
    c += 1
print(val_a // val_b)