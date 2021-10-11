import sys
num_input = int(sys.stdin.readline())
for cnt_ in range(1,num_input+1):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #' + str(cnt_) + ': '+str(A)+' + '+str(B)+' = '+str(A + B))