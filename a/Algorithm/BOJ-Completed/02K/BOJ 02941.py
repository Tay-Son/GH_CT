str_input = input()
lst_ca2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
lst_ca3 = ['dz=']

answer = 0

while str_input:
    if len(str_input) >= 3 and str_input[:3] in lst_ca3:
        str_input = str_input[3:]
    elif len(str_input) >= 2 and str_input[:2] in lst_ca2:
        str_input = str_input[2:]
    else:
        str_input = str_input[1:]
    answer += 1

print(answer)