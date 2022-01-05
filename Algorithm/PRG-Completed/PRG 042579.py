def solution(genres, plays):
    dct_genre_idx = dict()

    grd_genre_play = []
    cnt_genre = 0
    cnt_song = 0
    for genre, play in zip(genres, plays):
        if genre not in dct_genre_idx:
            dct_genre_idx[genre] = cnt_genre
            cnt_genre += 1
            grd_genre_play.append(list())
        idx_genre = dct_genre_idx[genre]
        grd_genre_play[idx_genre].append((play, cnt_song))
        cnt_song += 1

    def func(lst_):
        ret_ = 0
        for each_ in lst_:
            ret_ += each_[0]
        return ret_

    lst_answer = []
    grd_genre_play.sort(key=lambda x: func(x), reverse=True)
    for lst_genre_play in grd_genre_play:
        lst_genre_play.sort(key=lambda x:-x[0])
        for idx_ in range(min(2, len(lst_genre_play))):
            lst_answer.append(lst_genre_play[idx_][1])

    return lst_answer