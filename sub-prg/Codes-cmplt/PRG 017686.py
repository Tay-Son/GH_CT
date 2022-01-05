def solution(lst_file):
    def my_sort(str_file):
        ptr_n = 0
        while not '0' <= str_file[ptr_n] <= '9':
            ptr_n += 1
        ptr_t = ptr_n + 1
        while ptr_t < len(str_file) and '0' <= str_file[ptr_t] <= '9':
            ptr_t += 1
        return (str_file[:ptr_n].upper(), int(str_file[ptr_n:ptr_t]))

    lst_file.sort(key=lambda x: my_sort(x))

    return lst_file


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
