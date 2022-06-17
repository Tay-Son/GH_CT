import sys

S_ = int(sys.stdin.readline())
num_ = 1
cnt_ = 1
while num_ < S_ and num_ < (S_ - num_):
    print(S_)
    S_ -= num_
    num_ += 1
    cnt_ += 1
print(cnt_)
exit()
