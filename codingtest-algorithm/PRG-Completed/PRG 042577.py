def solution(phone_book):
    phone_book.sort()
    is_ = True
    for idx_ in range(len(phone_book)-1):
        len_ = len(phone_book[idx_])
        if phone_book[idx_]  == phone_book[idx_+1][:len_]:
            is_ = False
            break

    return is_