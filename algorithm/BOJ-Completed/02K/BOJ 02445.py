import sys
N = int(sys.stdin.readline())

for cnt_ in range(1,N):
    print('*'*cnt_ + ' '*((N-cnt_)*2)+'*'*cnt_)
for cnt_ in range(N,0,-1):
    print('*'*cnt_ + ' '*((N-cnt_)*2)+'*'*cnt_)