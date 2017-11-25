'''Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.'''
import math
def my_round(x):
    return int(x + math.copysign(0.5, x))


school_journal= [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
{'school_class': '4б', 'scores': [5,3,4,3,2]}, 
{'school_class': '4в', 'scores': [2,4,3,4,2]}, 
{'school_class': '5a', 'scores': [5,4,5,5,3]},
{'school_class': '5б', 'scores': [4,5,4,3,3]},
{'school_class': '6a', 'scores': [5,3,4,3,5]},
{'school_class': '6б', 'scores': [3,4,3,5,5]},
{'school_class': '7а', 'scores': [4,5,3,5,5]},
{'school_class': '8a', 'scores': [3,5,3,5,3]},
{'school_class': '8б', 'scores': [5,4,5,5,5]},
{'school_class': '8в', 'scores': [5,3,5,2,3]},
{'school_class': '9a', 'scores': [3,4,3,3,4]},
{'school_class': '9б', 'scores': [5,3,4,3,3]},
{'school_class': '9в', 'scores': [3,5,4,3,3]},
{'school_class': '10a', 'scores': [5,4,4,3,4]},
{'school_class': '11а', 'scores': [5,4,4,5,3]}]
sred_school = 0
for element in school_journal:
    #print(element['scores'])
    #print(element['school_class'])
    sred_class = sum(element['scores'])/len(element['scores'])
    print('средняя оценка по классам'+ '-'+ element['school_class']+ ':'+ str(my_round(sred_class)))
    sred_school = (sred_school + sred_class) 
    #for scores in element['scores']:
    #    print (scores)
sred_school = sred_school / len(school_journal)
print('средняя оценка по школе - ' + str(sred_school))
