cnt_iter = int(input())
for iter_ in range(cnt_iter):
    str_input = input()
    lst_input = [int(i) for i in str_input.split()]
    print(lst_input[0]+lst_input[1])