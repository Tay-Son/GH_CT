str_input = input()
lst_input = [int(i) for i in str_input.split()]

for num_ in range(1,10):
    print(str(lst_input[0])+' * '+str(num_)+' = '+str(lst_input[0]*num_))