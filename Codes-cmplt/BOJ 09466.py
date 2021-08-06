import sys

str_ = sys.stdin.readline().split()[0]
str_bomb = sys.stdin.readline().split()[0]

stk_ = []
lst_temp = []
lst_answer = []
for each_chr in str_:
    if len(stk_) and each_chr == str_bomb[stk_[-1]]:
        stk_[-1] += 1
        lst_temp.append(each_chr)
        if stk_[-1] == len(str_bomb):
            stk_.pop()
            for _ in range(len(str_bomb)):
                lst_temp.pop()
    elif each_chr == str_bomb[0]:
        stk_.append(1)
        lst_temp.append(each_chr)
        if stk_[-1] == len(str_bomb):
            stk_.pop()
            for _ in range(len(str_bomb)):
                lst_temp.pop()
    else:
        if len(lst_temp):
            lst_answer += lst_temp
            lst_temp.clear()
        lst_answer.append(each_chr)
        stk_.clear()

lst_answer += lst_temp

if lst_answer:
    print(''.join(lst_answer))
else:
    print('FRULA')
