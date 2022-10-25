s_dict = {}
count = 0
def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for symbol in str_:
        if symbol.isalpha() is True and symbol not in s_dict:
            s_dict[symbol] = 1
        elif symbol.isalpha() is True and symbol in s_dict:
            s_dict[symbol] += 1
    return s_dict

def get_char(s_dict):
    count = sum(s_dict.values())
    for s in s_dict:
        s_dict[s] = round(s_dict[s] / count * 100, 1)
    return s_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
# print(get_char(s_dict))
