import sys

for _ in range(int(sys.stdin.readline())):
    dct_ = dict()
    for _ in range(int(sys.stdin.readline())):
        trs_, key_ = sys.stdin.readline().split()
        if key_ not in dct_:
            dct_[key_] = 2
        else:
            dct_[key_] += 1
    tot_ = 1
    for each_ in dct_.values():
        tot_ *= each_
    print(tot_ - 1)

exit()
