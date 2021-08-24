def solution(K_, lst_room_number):
    import math

    cch_ = math.ceil(math.log2(K_ + 1))
    tre_ = [0 for _ in range(2 ** (cch_ + 1))]
    lst_answer = []
    for room_number in lst_room_number:
        stage_ = 1
        idx_tre = 1
        tre_[idx_tre] += 1
        while stage_ <= cch_:
            print(stage_, idx_tre, room_number)
            idx_tre *= 2
            div_, temp_room_number = divmod(room_number, 2 ** (cch_ - stage_))
            idx_tre += div_

            if tre_[idx_tre] == 2 ** (cch_ - stage_):
                idx_tre //= 2
                tre_[idx_tre] -= 1
                idx_tre //= 2
                room_number += 2 ** (cch_ - stage_)
                stage_ -= 1
            else:
                room_number = temp_room_number
                tre_[idx_tre] += 1
                stage_ += 1
        print(stage_, idx_tre, room_number)
        print(idx_tre - 2 ** cch_)
        lst_answer.append(idx_tre - 2 ** cch_)
        print()

    return lst_answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
exit()
