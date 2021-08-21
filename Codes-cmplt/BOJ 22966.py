import sys

N_ = int(sys.stdin.readline())
lst_ = []
for _ in range(N_):
    val_a, val_b = sys.stdin.readline().split()
    val_b = int(val_b)
    lst_.append((val_a, val_b))
lst_.sort(key=lambda x: x[1])
print(lst_[0][0])

exit()
