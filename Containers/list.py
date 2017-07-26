print('###---list---###')
# list:serveral ways to construct
# [] empty list
list_a=[]
# [a],[a,b,c] using commas to separate items
list_b=['i','love','China',666]
# list comprehension: [x for x in iterable]
list_c=[i for i in range(10)]
# list()
list_d=list('i love python')
# list(iterable)
list_e=list(range(10))
print(list_d)
print('list增加元素')
list_a.append('BeiJing') #append BeiJing to the end of sequence
list_a.append(['London','Washinton DC'])
list_b.insert(3,'!')   #insert an element at specified position
list_c.extend([11,12,'A','B','C']) #append serveral elements to the end of sequence
print(list_a)
print(list_b)
print(list_c)

print('list删除元素')
del list_a[0:2]
list_b.remove('!')
for i in range(5):
	list_c.pop(10)   #return and remove the value at specified position
list_a.clear()
print(list_a)
print(list_b)
print(list_c)

print('list修改元素')
list_c[0:10]=[0]*10  #[0]*10 equals [0,0,0,0,0,0,0,0,0,0]
list_c[0]=9
print(list_c)


# list sort
print('Before sort:',list_e)
list_e.sort(reverse=True)
print(list_e)

print('Before sort:',list_e)
list_e.sort(key=int)
print(list_e)

list_f=['3','11','255','127','-1']
list_f.sort(key= len and int)
print(list_f)
