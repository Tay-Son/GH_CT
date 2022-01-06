import sys
num_input = int(sys.stdin.readline())
for _ in range(num_input):
    lst_input = list(map(int,sys.stdin.readline().split()))
    num_student = lst_input[0]
    lst_input = lst_input[1:]
    avg_ = sum(lst_input)/len(lst_input)
    cnt_ = 0
    for each_ in lst_input:
        if each_ > avg_:
            cnt_ += 1
    print(format(cnt_/len(lst_input) * 100,'.3f')+'%')