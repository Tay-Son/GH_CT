val_input = int(input())

is_ = False
for cnt_ in range(val_input//5,-1,-1):
    val_temp = val_input - cnt_ * 5
    if not val_temp % 3:
        print(cnt_ + val_temp//3)
        is_ = True
        break

if not is_:
    print(-1)