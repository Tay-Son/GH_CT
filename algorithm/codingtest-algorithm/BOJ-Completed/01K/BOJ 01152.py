import sys

str_ = sys.stdin.readline().strip()
if len(str_):
    print(str_.count(' ') + 1)
else:
    print(0)
exit()
