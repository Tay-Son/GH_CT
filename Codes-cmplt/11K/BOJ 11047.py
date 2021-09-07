import sys

N, K = map(int, sys.stdin.readline().split())
lst_ = []
for _ in range(N):
    lst_.append(int(sys.stdin.readline()))
lst_.reverse()

answer_ = 0
for each_ in lst_:
    answer_ += K // each_
    K %= each_

print(answer_)
