str_input = input()
val_input = int(str_input)

if val_input % 400 == 0:
    print('1')
elif val_input % 4 == 0 and val_input % 100 != 0:
    print('1')
else:
    print('0')