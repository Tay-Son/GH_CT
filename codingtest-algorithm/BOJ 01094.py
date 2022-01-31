import sys
from collections import Counter

print(Counter(bin(int(sys.stdin.readline()))[2:])['1'])

exit()
