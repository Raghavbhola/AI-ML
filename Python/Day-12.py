#--------------------------[ Nov. 16, 2026 ]-----------------------------


#Map, filter and reduce
num = [1,2,3,4,5,6]
sqr = list(map(lambda nums:nums**2,num))
print(sqr)

names = ['kunal', 'lavisha', 'ravi', 'meena', 'rakesh']

#caps = list(map(str.upper, names))
caps = list(map(lambda name:name.upper(), names))
print(caps)

#Filters
num = [1,2,3,4,5,6,7,8,9,10]
even_num = list(filter(lambda filt:filt%2 == 0,num))
print(even_num)

num = [1,2,3,4,5,6,7,8,9,10]
even_num = list(filter(lambda filt:filt%2 == 0,num))
print(even_num)

score = [12,34,224,663,7,25,256,3514,67]
pass_st = list(filter(lambda score:score>80,score))
print(pass_st)

#from functools import reduce
num = [10,20,30,40,50]
total = reduce(lambda first,second:first+second, num)
print(total)

numbers = [10, 20, 30, 40,50]
multiple = reduce(lambda first, second: first*second, numbers)
print(multiple)

#filter and map combination
name = ['kunal', 'avisha', 'ravi', 'meena', 'rakesh', 'isha', 'uma']
vow_upper = list(map(lambda up:up.upper(), filter(lambda n: n.startswith(('a', 'e', 'i', 'o', 'u')),name)))
print(vow_upper)
