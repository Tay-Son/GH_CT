import sys

N, X = map(int, sys.stdin.readline().split())
lst_ = map(int, sys.stdin.readline().split())
lst_answer = []
for each_ in lst_:
    if each_ < X:
        lst_answer.append(str(each_))
print(' '.join(lst_answer))
