import sys
input_ = int(sys.stdin.readline())
for cnt_ in range(1,input_+1):
    print(' '*(input_-cnt_)+'*'*cnt_)