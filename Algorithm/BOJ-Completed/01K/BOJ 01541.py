import sys

str_input = sys.stdin.readline()

lst_ = []
str_temp = ''
for each_ in str_input:
    if each_ in ['-', '+']:
        lst_.append(int(str_temp))
        str_temp = ''
    str_temp += each_
lst_.append(int(str_temp))

sum_ = 0
is_ = False
for each_ in lst_:
    if is_:
        each_ = -abs(each_)
    elif each_ < 0:
        is_ = True
    sum_ += each_
print(sum_)

exit()