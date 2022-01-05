import sys

set_a = set()
set_b = set()
for _ in range(3):
    a, b = sys.stdin.readline().split()
    if a in set_a:
        set_a.remove(a)
    else:
        set_a.add(a)
    if b in set_b:
        set_b.remove(b)
    else:
        set_b.add(b)
print(set_a.pop(), set_b.pop())
