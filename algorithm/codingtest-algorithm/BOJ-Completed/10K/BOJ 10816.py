import sys
from collections import Counter
N = int(sys.stdin.readline())
lst_cards = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
lst_targets = list(map(int,sys.stdin.readline().split()))

dct_cards = Counter(lst_cards)

lst_answer = []
for target in lst_targets:
    if target in dct_cards:
        lst_answer.append(str(dct_cards[target]))
    else:
        lst_answer.append('0')

print(' '.join(lst_answer))