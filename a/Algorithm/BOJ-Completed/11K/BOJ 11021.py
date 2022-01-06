import sys
num_input = int(sys.stdin.readline())
for cnt in range(1,num_input+1):
    A, B = map(int,sys.stdin.readline().split())
    print('Case #'+str(cnt)+': '+str(A+B))