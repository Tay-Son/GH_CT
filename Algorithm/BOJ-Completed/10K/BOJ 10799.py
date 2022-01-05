import sys

str_input = sys.stdin.readline()
str_input = str_input.replace('()', 'C')
cnt_ = 0
answer_ = 0
for each_ in list(str_input):
    if each_ == '(':
        cnt_ += 1
    elif each_ == ')':
        cnt_ -= 1
        answer_ += 1
    else:
        answer_ += cnt_

print(answer_)
