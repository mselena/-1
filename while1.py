'''Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретите имя "Валера". Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop()'''
'''name_list= ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
i = 0
while name_list[i] != 'Валера':
    print(str(i) +' '+name_list[i]+' - это не Валера!')
    i = i + 1
print('Валера нашелся!')'''

def find_person():
    name_list= ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
    name = input('введите имя: ')
    i = 0
    while True:
        i = i + 1
        if i == len(name_list):
            print(name+' тут нет')
            break
        if name == name_list[i]:
            print(name+ ' нашелся!')
            break
        #else:
            #print(str(i) +' '+name_list[i]+' - это не '+ name

def get_answer():
    question= input('')
    answers= {'привет': 'и тебе привет!', 'как дела': 'лучше всех', 'пока': 'увидимся','Пока!': 'увидимся'}
    if question in answers:
        print(answers[question])
        return answers[question]
    else:
        print('не понял')
        return 'не понял'



def ask_user():
    cmd = get_answer()
    while cmd != 'увидимся':
        cmd = get_answer()

'''Переписать функцию ask_user(), добавив обработку exception-ов
Добавить перехват ctrl+C и прощание'''

try:
    ask_user()
except KeyboardInterrupt:
    print(' поки')
