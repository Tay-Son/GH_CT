import sys

num_input = int(sys.stdin.readline())
lst_ = [0 for _ in range(10001)]
for _ in range(num_input):
    lst_[int(sys.stdin.readline())] += 1
for idx_ in range(len(lst_)):
    for _ in range(lst_[idx_]):
        print(idx_)