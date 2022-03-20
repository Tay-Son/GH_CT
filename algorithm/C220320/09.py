import sys

DIV_ = 1000003

K_ = int(sys.stdin.readline()) - 1

curr_ = 0
for num_ in range(1, K_ + 1):
    curr_ = curr_ * 4 + 2 ** num_ - 1
    curr_ %= DIV_

print(curr_)
exit()
