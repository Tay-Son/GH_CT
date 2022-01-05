str_input = input()
lst_input = [int(i) for i in str_input.split()]

lst_input[1] -= 45
if lst_input[1] < 0:
    lst_input[1] = 60 + lst_input[1]
    lst_input[0] -= 1
    if lst_input[0] < 0:
        lst_input[0] = 24 + lst_input[0]
print(str(lst_input[0])+' '+str(lst_input[1]))