def solution(mat_score):
    N_ = len(mat_score)
    grd_sum = [[] for _ in range(N_)]

    for idx_student_c in range(N_):
        for idx_student_p in range(N_):
            if idx_student_c != idx_student_p:
                grd_sum[idx_student_c].append(mat_score[idx_student_p][idx_student_c])
        grd_sum[idx_student_c] = sorted(grd_sum[idx_student_c])
        temp_ = mat_score[idx_student_c][idx_student_c]
        if not (temp_ < grd_sum[idx_student_c][0] or temp_ > grd_sum[idx_student_c][-1]):
            grd_sum[idx_student_c].append(temp_)

    str_grade = ''
    for lst_sum in grd_sum:
        temp_ = sum(lst_sum) / len(lst_sum)
        print(temp_)
        if temp_ >= 90:
            str_grade += 'A'
        elif temp_ >= 80:
            str_grade += 'B'
        elif temp_ >= 70:
            str_grade += 'C'
        elif temp_ >= 50:
            str_grade += 'D'
        else:
            str_grade += 'F'

    return str_grade


print(solution(
    [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
