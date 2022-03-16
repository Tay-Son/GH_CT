import sys

input_ = sys.stdin.readline().split()[0]
while input_ != '0':
    is_ = True
    len_ = len(input_)
    for cnt_ in range(len_ // 2):
        if input_[cnt_] != input_[len_ - cnt_ - 1]:
            is_ = False
            break
    if is_:
        print('yes')
    else:
        print('no')
    input_ = sys.stdin.readline().split()[0]