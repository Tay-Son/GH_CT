import sys

num_input = int(sys.stdin.readline())
for _ in range(num_input):
    cnt_, str_ = sys.stdin.readline().split()
    for each_chr in str_:
        for _ in range(int(cnt_)):
            print(each_chr,end='')
    print()