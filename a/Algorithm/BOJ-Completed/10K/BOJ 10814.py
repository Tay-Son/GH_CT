import sys

num_input = int(sys.stdin.readline())
lst_ = []
for _ in range(num_input):
    lst_.append(sys.stdin.readline().split())
lst_.sort(key=lambda x: int(x[0]))
for each_ in lst_:
    print(' '.join(each_))