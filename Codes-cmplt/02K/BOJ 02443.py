import sys
N = int(sys.stdin.readline())

for cnt_ in range(N,0,-1):
    print(' '*(N-cnt_)+'*'*(cnt_*2-1))