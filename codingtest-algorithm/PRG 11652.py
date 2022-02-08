import sys
from collections import Counter

lst_ = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
print(sorted(sorted(list(Counter(lst_).items()), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)[0][0])

exit()
