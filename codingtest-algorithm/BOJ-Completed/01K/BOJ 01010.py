num_input = int(input())
for _ in range(num_input):
    N, M = map(int, input().split())
    N = min(N, M-N)
    Val_A, Val_B = 1, 1
    for cnt_ in range(N):
        Val_A *= M
        Val_B *= N
        M -= 1
        N -= 1
    print(Val_A//Val_B)