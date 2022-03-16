str_input = input()
while str_input != '0 0':
    val_A, val_B = [int(i) for i in str_input.split()]
    print(val_A + val_B)
    str_input = input()