import sys
input_ = int(sys.stdin.readline())
curr = (input_ % 10) * 10 + ((input_ // 10 + input_ % 10) % 10)
answer = 1

while not curr == input_:
    curr = (curr % 10) * 10 + ((curr // 10 + curr % 10) % 10)
    answer += 1

print(answer)