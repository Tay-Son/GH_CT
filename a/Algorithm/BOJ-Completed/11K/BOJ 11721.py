str_input = input()

while len(str_input) > 10:
    print(str_input[:10])
    str_input = str_input[10:]
print(str_input)