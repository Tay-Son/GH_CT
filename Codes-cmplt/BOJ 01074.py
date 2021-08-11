import sys

N, r, c = map(int, sys.stdin.readline().split())

answer_ = 0
for each_ in range(N - 1, -1, -1):
    temp_ = 2 ** each_

    if c // temp_:
        answer_ += temp_ ** 2
    if r // temp_:
        answer_ += 2 * (temp_ ** 2)

    c %= temp_
    r %= temp_

print(answer_)