'''Написать функцию, которая принимает на вход две строки.
Если строки одинаковые, возвращает 1.
Если строки разные и первая длиннее, возвращает 2.
Если строки разные и вторая строка 'learn', возвращает 3.'''
def stringi(string1,string2):
    if string1 == string2:
        print('1')
    else: 
        if len(string1) > len(string2):
            print('2')
        if string2 == 'learn':
            print('3')



string1= input('')
string2= input('')
stringi(string1,string2)