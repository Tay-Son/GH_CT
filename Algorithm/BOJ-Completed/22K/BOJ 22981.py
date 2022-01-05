import sys

N_, K_ = map(int, sys.stdin.readline().split())
lst_ = list(map(int, sys.stdin.readline().split()))
lst_.sort()

min_ = K_
for ptr_ in range(1, N_):
    val_a = lst_[0] * ptr_
    val_b = lst_[ptr_] * (N_ - ptr_)
    throughput_ = val_a + val_b
    val_a, val_b = divmod(K_, throughput_)
    min_ = min(min_, val_a + (val_b != 0))

print(min_)

exit()
