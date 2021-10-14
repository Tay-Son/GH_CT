lst_fib = [0, 1]

input_ = int(input())
if input_ < 2:
    print(lst_fib[input_])
else:
    for _ in range(input_-1):
        lst_fib.append(lst_fib[-1]+lst_fib[-2])
    print(lst_fib[-1])