import sys
import re

for _ in range(int(sys.stdin.readline())):
    str_ = sys.stdin.readline().strip()
    re_ = re.compile('(100+1+|01)+$')
    if re_.match(str_):
        print('YES')
    else:
        print('NO')
exit()
