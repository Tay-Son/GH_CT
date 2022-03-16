import sys

N = int(sys.stdin.readline())
lst_ = []
for _ in range(N):
    s_, e_ = map(int, sys.stdin.readline().split())
    lst_.append([s_, e_])

lst_.sort(key=lambda x: x[0])
lst_.sort(key=lambda x: x[1])

answer_ = 0
curr_ = 0
for each_ in lst_:
    if each_[0] >= curr_:
        curr_ = each_[1]
        answer_ += 1

print(answer_)