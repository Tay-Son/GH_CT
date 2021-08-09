import sys

cnt_ = 0
dct_ = {}

str_input = sys.stdin.readline().rstrip()
while str_input:
    if str_input not in dct_:
        dct_[str_input] = 0
    dct_[str_input] += 1
    cnt_ += 1
    str_input = sys.stdin.readline().rstrip()

for a_, b_ in sorted(dct_.items()):
    print('{0} {1:0.4f}'.format(a_, b_ * 100 / cnt_))

exit()