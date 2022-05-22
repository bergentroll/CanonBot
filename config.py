import random


def mainconfig(txt_file):
    with open(txt_file, "r") as f:
        contents = f.read()
        text_split = contents.split('___separator___')
        sn = random.randint(0, len(text_split) - 1)
        result = text_split[sn]
        return result


def delimiter(print_text, limit):
    index = []
    сom_index = print_text.index('<u>')
    for x in range(0, сom_index, limit):
        i = print_text.index(" ", x, limit + x)
        index.append(i)
    return index


###################################################################
token = '5151139838:AAF014XgtqS0_OgmzJNP5yEJ-gSWUUFw9mg'

main_menu = """
Выберите раздел

Любой: /all_sutta
Дхаммапада: /dhammapada_sutta
Тхерагатха: /theragatha_sutta
Тхеригатха: /therigatha_sutta
Итивуттака: /itivuttaka_sutta
Удана: /udana_sutta

Инфо: /about_us"""

about_text = (
    'Этот бот создан для некоммерческого использования, все материалы взяты с сайта theravada.ru.'
    '\n\n'
    'Наша <a href="https://theravada.ru/blessings.htm">община</a> существует на пожертвования,'
    ' вы можете сделать дану на карту сбербанка 4276 5500 2002 5576.'
    '\n\n'
    'По вопросам и предложениям пишите @Alexandr_Cherkaev и @Max_Kotebus')

######################################################################
