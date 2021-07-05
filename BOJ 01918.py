import sys

str_ = sys.stdin.readline().rstrip()
stk_ = []
str_answer = ''

for chr_ in str_:
    if chr_ in ["+", "-", "*", "/"]:
        stk_.append(chr_)
    elif chr_ == '(':
        stk_.append(chr_)
    elif chr_ == ')':
        lst_p = []
        lst_o = []

        lst_p.append(stk_.pop())
        while stk_[-1] != '(':
            lst_o.append(stk_.pop())
            lst_p.append(stk_.pop())
        stk_.pop()

        stk_.append(''.join(reversed(lst_p)) + ''.join(lst_o))
    else:
        stk_.append(chr_)
lst_p = []
lst_o = []

lst_p.append(stk_.pop())
while stk_:
    lst_o.append(stk_.pop())
    lst_p.append(stk_.pop())

stk_.append(''.join(reversed(lst_p)) + ''.join(lst_o))

print(stk_[-1])

exit()
