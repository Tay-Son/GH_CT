def solution(lst_str, lst_language, lst_pref):
    dct_job = {
        'SI': 0,
        'CONTENTS': 0,
        'HARDWARE': 0,
        'PORTAL': 0,
        'GAME': 0
    }

    dct_lang_pref = {language_: pref for language_, pref in zip(lst_language, lst_pref)}

    for each_str in lst_str:
        lst_split = each_str.split()
        target_job = lst_split[0]
        for language_, score in zip(lst_split[1:], range(5, 0, -1)):
            if language_ in dct_lang_pref:
                dct_job[target_job] += dct_lang_pref[language_] * score

    return sorted(sorted(list(dct_job.items())), key=lambda x_: x_[1], reverse=True)[0][0]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#",
                "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"],
               ["PYTHON", "C++", "SQL"],
               [7, 5, 5]))
