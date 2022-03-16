import sys

str_ = sys.stdin.readline().rstrip()
stk_ = []
str_answer = ''

for chr_ in str_:
    if chr_ in ["+", "-"]:
        while stk_ and stk_[-1] != '(':
            str_answer += stk_.pop()
        stk_.append(chr_)
    elif chr_ in ["*", "/"]:
        while stk_ and stk_[-1] in ["*", "/"]:
            str_answer += stk_.pop()
        stk_.append(chr_)
    elif chr_ == '(':
        stk_.append(chr_)
    elif chr_ == ')':
        while stk_ and stk_[-1] != '(':
            str_answer += stk_.pop()
        stk_.pop()
    else:
        str_answer += chr_

while stk_:
    str_answer += stk_.pop()
print(str_answer)

exit()
