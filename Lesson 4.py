# Задание 1 (easy)

# a = [i for i in range(-10, 10)]
# b = [i**2 for i in a]
# print(a)
# print(b)

# Задание 2 (easy)

# a = ['яблоко', 'киви', 'банан', 'персик', 'ананас']
# b = ['нектарин', 'персик', 'малина', 'клубника', 'киви']
# c = list(set(a) & set(b))
# print(c)

# Задание 3 (easy)

# import copy
# a = [i for i in range(-10, 10)]
# b = copy.deepcopy(a)
# b = [el for el in a if el % 3 == 0 and el >=0 and el % 4 !=0]
# print(a)
# print(b)

# Задание 1 (normal)

# import re

# pattern_name = '([A-ZА-Я][a-zа-я])'
# pattern_surname = '([A-ZА-Я][a-zа-я])'
# pattern_email = '([a-z_0-9]+@+[a-z0-9]+\.(ru|org|com))'

# name = input('Ввеждите ваше имя с большой буквы: ')
# result_name = re.match(pattern_name, name)
# surname = input('Ввеждите вашу фамилию с большой буквы: ')
# result_surname = re.match(pattern_surname, surname)
# email = input('Ввеждите вашу почту: ')
# result_email = re.findall(pattern_email, email)

# result_name = re.match(pattern_name, name)
# result_surname = re.match(pattern_surname, surname)
# result_email = re.findall(pattern_email, email)

# if result_name:
#     if result_surname:
#         if result_email:
#             print('Все верно указано')
#         else:
#             print('Не верно указана почта!')
#     else:
#         print('Не верно указана фамилия!')
# else:
#     print('Не верно указано Имя')

# Задание 2 (normal)

import re

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

pattern_dots = '\.{2,}'
result = re.search(pattern_dots, some_str)
if result:
    print('В тексте есть больше одной точки подряд!')
else:
    print('В тексте нет больше одной точки подряд')

