import sys
num_input = int(sys.stdin.readline())
lst_ = []
for _ in range(num_input):
    lst_.append(int(sys.stdin.readline()))
lst_.sort()
for each_ in lst_:
    print(each_)