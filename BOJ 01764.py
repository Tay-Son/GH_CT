import sys

N, M = map(int, sys.stdin.readline().split())
set_ = set()
for _ in range(N):
    set_.add(sys.stdin.readline().split()[0])

lst_dbj = []
for _ in range(M):
    str_input = sys.stdin.readline().split()[0]
    if str_input in set_:
        lst_dbj.append(str_input)

lst_dbj.sort()
print(len(lst_dbj))
for each_ in lst_dbj:
    print(each_)
