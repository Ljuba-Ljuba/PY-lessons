
"""
+7 911 279 02 46
+7 999 210 02 46

PY itmo! вк клуб
"""
# переменная
#PEP8
is_student=True

name=input('Введите имя:')
print('hello,',name,'!')

#Что такое типы данных?
#Скалярные типы хранятся в стэке. только 1 значение в момент времени возможно
#bool- логические (True или False)

#int-целочисленные
i1=666
i2=0x59 #шестнадцатиричная система исчисления
i3=0b0101111 #двоичная система
i4=0o255 #восьмиричная СС

#float-с плавающей точкой
f1=1.23
f2=12e-3 #12x10^-3
f3=12e3#12x10^3

#str-строковый
#bytes - байтовая строка
s1='some string' #лучше
s2="some \"sstring"
s3=r'Raw string' #сырая строка - неизменяемая. для регулярных выражений
s4=u'Hello' #для второго питона перевод в юникод
S5=b'bites' #байтовая строка
s6='''

''' # переносы и неизменяемый вид
s7="""

"""
#комплексные числа - complex
с1=3.14j


#Структурированные - могут содержать несколько значений в один период времени. как скалярные, так и структурированные
#tuple, list, set, dict, object
#object - позже
#tuple - кортеж
t1=(1,)
t2=(True,1,3.45,'string',(1,2,3)) #можно хранить разные типы данных
#list - списки
lst1=[[1],[2],3,False, ()]

#set  множества
s1={1,2,3} #фигурные скобки!
s2=set([100,5,1]) 
s3=set() #пустое множество
s4=s1-{1,2}
# упорядочивает
# в множестве тольо уникальные данные. повторы исключаются
print (s4)
print(s2)
print(t2[1],lst1[2],lst1[0]) # обращение к элементам в кортежах, списках  по индексу. от 0  начиная

# вопрос
# dict словари
d={} # просто фигурные скобки - словарь

d={
    'id':1,
	'name':'Вася',
	'is_student':True,
	'skills':('python', 'linux')
}

#специальные типы: 
#None - пустота
a=None #просто написать а нельзя

















