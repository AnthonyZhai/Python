print('###---tuple---###')
# tuple:serveval ways to construct
# () empty tuple
tuple_a=()
# a, (a,) a singleton tuple
tuple_b=('a',)   #this is the way to construct a singleton tuple,equals 
tuple_b='a',
# a,b,c (a,b,c) using commas separate items
tuple_c=1,2,3
tuple_c=(1,2,3)
# tuple(iterable)
tuple_d=tuple(range(5))
tuple_d=tuple([i for i in range(5)])
tuple_d=tuple([0,1,2,3,4])
# tuple()
tuple_a=tuple()

"""
from collections import Iterable
print(isinstance(range(5),Iterable)) 
print(isinstance([i for i in range(5)],Iterable))

"""
print(tuple_a)
print(tuple_b)
print(tuple_c)
print(tuple_d)