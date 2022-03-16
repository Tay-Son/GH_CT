import sys

set_ = set()
N_, M_ = map(int, sys.stdin.readline().split())
for _ in range(N_):
    str_input = sys.stdin.readline().rstrip()
    set_.add(str_input)
ans_ = 0
for _ in range(M_):
    str_input = sys.stdin.readline().rstrip()
    ans_ += str_input in set_
print(ans_)
exit()