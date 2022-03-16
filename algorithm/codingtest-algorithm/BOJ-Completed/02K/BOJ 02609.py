input_a, input_b = map(int, input().split())

for val_ in range(min(input_a, input_b), 0, -1):
    if not input_a % val_ and not input_b % val_:
        print(val_)
        break

temp_a = input_a
temp_b = input_b
while not temp_a == temp_b:
    if temp_a > temp_b:
        temp_b += input_b
    else:
        temp_a += input_a
print(temp_a)