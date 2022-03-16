import sys

num_input = int(sys.stdin.readline())
lst_ = []
for _ in range(num_input):
    val_x, val_y = sys.stdin.readline().split()
    lst_.append([val_x, val_y])

lst_.sort(key=lambda x: int(x[1]))
lst_.sort(key=lambda x: int(x[0]))

for each_ in lst_:
    print(' '.join(each_))