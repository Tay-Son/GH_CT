import sys
num_input = int(sys.stdin.readline())
lst_ = []
for _ in range(num_input):
    lst_.append(int(sys.stdin.readline()))
for each_ in sorted(lst_):
    print(each_)