str_input = input()
lst_output = []
for each_ in range(26):
    chr_ = chr(each_ + ord('a'))
    if chr_ in str_input:
        lst_output.append(str(str_input.index(chr_)))
    else:
        lst_output.append(str(-1))

print(' '.join(lst_output))