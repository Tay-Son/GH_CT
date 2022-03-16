import sys

str_a, str_b = sys.stdin.readline().split()
lst_a = []
lst_b = []
for idx_a in range(6, len(str_a), 6):
    lst_a.append(int(str_a[idx_a:idx_a + 6]))
if idx_a:
    lst_a.append(int(s))

for idx_b in range(6, len(str_b), 6):
    lst_b.append(int(str_b[idx_b:idx_b + 6]))
exit()
