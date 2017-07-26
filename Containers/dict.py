print('###---dict---###')
# dict: serveral ways to construct
# {key:value}
dict_a={'one':1,'two':2,'three':3}
# dict(mapping,**kwarg)
dict_b=dict(one=1,two=2,three=3)
# dict(**kwarg)
dict_b=dict({'one':1,'two':2,'three':3})
# dict(iterable,**kwarg)
dict_c=dict([('one',1),('two',2),('three',3)])
print(dict_a)
print(dict_b)
print(dict_c)

print('###---operations of dict---###')
# len(d)
print(len(dict_a))
# d[key]
print(dict_b['two'])
try:
	print(dict_c['four'])
except KeyError:
	print('Can\'t return value according to the key given by user,KeyError')
# d[key]=value
dict_a['one']='one'
dict_a['four']=4
print(dict_a)
# del d[key]
del dict_a['four']
# key (not) in d
print('four' in dict_b)
print('one' in dict_a)
# iter(d)
key_iter=iter(dict_c)
for i in key_iter:
	print(i)
# clear()
dict_c.clear()
# copy()
dict_d=dict_a.copy()
# fromkeys(seq[,value])
seq=('Chinese','Math','English')
dict_e=dict.fromkeys(seq,100)
print(dict_e)
# get(key[,default])
print(dict_a.get('two'))
# items()
for key,value in dict_a.items():
	print(key,value)
# keys()
for i in dict_b.keys():
	print(i)
# pop(key[,default])
print(dict_a.pop('two'))
print(dict_a.pop('two',-1))
try:
	print(dict_a.pop('two'))
except KeyError:
	print('Can\'t remove and return value,and default is not given,KeyError')
# popitem()
print(dict_a.popitem())
try:
	print(dict_c.popitem())
except KeyError:
	print('Can\'t remove and return (key,value) pair because of dictionary is empty,KeyError')
# setdefault(key[,default])
dict_c.setdefault('one',1)
dict_c.setdefault('two')
print(dict_c)
# update([other])
dict_c.update(dict_e)
print(dict_c)
# values()
print(dict_c.values())
#
# Dcitionary view objects
# which are returned by dict.keys(),dict.values() and dict.items()
# len(dictview)
keys=dict_e.keys()
values=dict_e.values()
print(keys)
print(values)

# iter(dictview)
# x in dictview