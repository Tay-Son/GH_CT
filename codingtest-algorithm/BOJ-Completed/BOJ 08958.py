import sys
num_input = int(sys.stdin.readline())
for _ in range(num_input):
    str_input = sys.stdin.readline()
    val_r = 0
    answer = 0
    for each_chr in str_input:
        if each_chr == 'O':
            val_r += 1
            answer += val_r
        if each_chr == 'X':
            val_r = 0
    print(answer)