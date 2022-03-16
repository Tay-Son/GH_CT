import sys

num_input = int(sys.stdin.readline())

set_ = set()
for _ in range(num_input):
    set_.add(sys.stdin.readline().split()[0])

for each_ in sorted(sorted(list(set_)), key=lambda x: len(x)):
    print(each_)

exit()