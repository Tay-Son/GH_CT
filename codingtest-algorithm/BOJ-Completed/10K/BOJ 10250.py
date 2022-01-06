num_input = int(input())
for cnt_ in range(num_input):
    H, W, N = map(int,input().split())
    N -= 1
    print(str(N % H+1) + str(N // H+1).zfill(2))