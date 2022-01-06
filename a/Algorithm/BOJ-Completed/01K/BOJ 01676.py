input_ = int(input())
fact_ = 1
answer = 0
for cnt_ in range(1, input_ + 1):
    fact_ *= cnt_
    while not fact_ % 10:
        fact_ //= 10
        answer += 1
print(answer)
