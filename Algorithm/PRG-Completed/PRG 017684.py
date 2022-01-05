def solution(str_msg):
    tri_tpl = [-1 for _ in range(26)]
    tri_ = [tri_tpl.copy()]

    print(tri_)
    for cnt_ in range(26):
        tri_.append(tri_tpl.copy())
        tri_[0][cnt_] = len(tri_) - 1

    print(tri_[0])

    lst_answer = []
    idx_tri = 0
    for each_chr in str_msg:
        ptr_ = ord(each_chr) - ord('A')
        idx_temp = tri_[idx_tri][ptr_]
        if idx_temp != -1:
            idx_tri = idx_temp
        else:
            lst_answer.append(idx_tri)
            tri_.append(tri_tpl.copy())
            tri_[idx_tri][ptr_] = len(tri_) - 1
            idx_tri = tri_[0][ptr_]
    lst_answer.append(idx_tri)

    return lst_answer


print(solution("ABABABABABABABAB"))
