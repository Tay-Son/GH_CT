input_ = int(input())

cnt_answer = 0
for each_ in range(1,input_+1):
    each_ = str(each_)
    if len(each_) > 1:
        val_d = int(each_[0]) - int(each_[1])
        is_ = True
        for idx_ in range(1, len(each_) - 1):
            if not int(each_[idx_]) - int(each_[idx_ + 1]) == val_d:
                is_ = False
                break
        if is_:
            cnt_answer += 1
    else:
        cnt_answer += 1

print(cnt_answer)