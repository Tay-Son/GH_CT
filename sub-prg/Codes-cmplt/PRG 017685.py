def solution(lst_word):
    tri_t = [0 for _ in range(27)]
    tri_ = [tri_t.copy()]

    for word_ in lst_word:
        idx_tri = 0
        for each_chr in word_:
            tri_[idx_tri][26] += 1
            idx_chr = ord(each_chr) - ord('a')
            if not tri_[idx_tri][idx_chr]:
                tri_[idx_tri][idx_chr] = len(tri_)
                tri_.append(tri_t.copy())
            idx_tri = tri_[idx_tri][idx_chr]
        tri_[idx_tri][26] += 1

    tot_ = 0
    for word_ in lst_word:
        idx_tri = 0
        for each_chr in word_:
            if tri_[idx_tri][26] == 1:
                break
            else:
                idx_chr = ord(each_chr) - ord('a')
                idx_tri = tri_[idx_tri][idx_chr]
                tot_ += 1

    return tot_


print(solution(["word", "war", "warrior", "world"]))
