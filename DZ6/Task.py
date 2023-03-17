#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint as RR

n = int(input('задайте длину списка:'))
# my_list = []
# for i in range(n):
#     a = random.randint(0, 10)
#     my_list.append(a)
# print(my_list)
# sum_el = 0
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         sum_el += my_list[i]

# print(sum_el)

my_list4=[RR(0,10) for i in range(n)]
print(my_list4)
res=sum([my_list4[i] for i in range(len(my_list4)) if i%2!=0])
print(res)


#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

n = int(input('задайте длину списка:'))
# my_list = []
# for i in range(n):
#     a = RR(0, 10)
#     my_list.append(a)
# print(my_list)
l=0
# if n%2==0:
#     l=(n/2)
# else:
#     l=n/2
#     l=int(l)+1
# my_list2=[]
# for i in range(int(l)):
#     p=my_list[i]*my_list[len(my_list)-i-1]
#     my_list2.append(p)
# print(my_list2)

my_lst=[]
my_lst=([RR(0,10) for i in range(n)])
print(my_lst)
rez=n/2 if n%2==0  else ((n/2)+1)
print(rez)
my_list2=[my_lst[i]*my_lst[len(my_lst)-i-1] for i in range(int(rez)) ]
print(my_list2)





