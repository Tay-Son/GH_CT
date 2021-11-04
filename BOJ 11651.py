import sys

lst_ = []
for _ in range(int(sys.stdin.readline())):
    lst_.append(tuple(map(int, sys.stdin.readline().split())))
lst_.sort(key=lambda x: x[0])
lst_.sort(key=lambda x: x[1])
for x_, y_ in lst_:
    print(x_, y_)

exit()
