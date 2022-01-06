num_input = int(input())

lst_fib = [0, 1]
if num_input >= 2:
    for _ in range(2, num_input+1):
        lst_fib.append(lst_fib[-1] + lst_fib[-2])
print(lst_fib[num_input])