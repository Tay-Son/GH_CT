import sys

for _ in range(int(sys.stdin.readline())):
    R_, C_ = map(int, sys.stdin.readline().split())
    lst_ = []
    for _ in range(R_):
        in_ = sys.stdin.readline().rstrip()
        lst_.append(in_[::-1])
    for each_ in lst_:
        print(each_)

exit()
