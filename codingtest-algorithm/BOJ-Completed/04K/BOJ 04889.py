import sys

cnt_ = 0
str_input = sys.stdin.readline().strip()
while str_input[0] != '-':
    cnt_ += 1
    tot_ = 0

    val_bank = 0
    val_remain = len(str_input) - 1
    for chr_ in str_input:
        if chr_ == '{':
            if val_bank > val_remain:
                tot_ += 1
                val_bank -= 1
            else:
                val_bank += 1
        else:
            if not val_bank:
                tot_ += 1
                val_bank += 1
            else:
                val_bank -= 1
        val_remain -= 1
    print(str(cnt_) + '. ' + str(tot_))

    str_input = sys.stdin.readline().strip()

exit()
