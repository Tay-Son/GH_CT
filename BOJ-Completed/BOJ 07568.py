import sys

N = int(sys.stdin.readline())
lst_ = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst_.append([x, y])

lst_answer = []
for each_ in lst_:
    cnt_ = 1
    for each_2 in lst_:
        if each_[0] < each_2[0] and each_[1] < each_2[1]:
            cnt_ += 1
    lst_answer.append(cnt_)

print(' '.join(map(str, lst_answer)))