import sys

lst_str = []
str_input = sys.stdin.readline()
while str_input != '.\n':
    lst_str.append(str_input[:-1])
    str_input = sys.stdin.readline()

for each_str in lst_str:
    stk_ = []
    is_ = True
    for each_chr in each_str:
        if each_chr in ['(', '[']:
            stk_.append(each_chr)
        elif each_chr == ')':
            if len(stk_) > 0:
                if stk_.pop(-1) != '(':
                    is_ = False
                    break
            else:
                is_ = False
                break
        elif each_chr == ']':
            if len(stk_) > 0:
                if stk_.pop(-1) != '[':
                    is_ = False
                    break
            else:
                is_ = False
                break
    if len(stk_) > 0:
        is_ = False
    if is_:
        print('yes')
    else:
        print('no')