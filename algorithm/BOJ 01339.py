import sys

dct_ = {}

for _ in range(int(sys.stdin.readline())):
    str_ = sys.stdin.readline().strip()
    mag_ = 1
    for each_chr in reversed(str_):
        print(each_chr)
        if each_chr not in dct_:
            dct_[each_chr] = mag_
        else:
            dct_[each_chr] += mag_
        mag_ *= 10

print(dct_)

ans_ = 0
lst_ = sorted(dct_.values(), reverse=True)
print(lst_)
for mag_, val_ in zip(range(9, 9 - len(lst_), -1), lst_):
    ans_ += mag_ * val_

print(ans_)

exit()
