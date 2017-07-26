print('###---set types---###')
print('###---set---###')
# set:two ways to construct
# {}
set_a={'Anderson','Anthony','GaoSir','RushChu'}
# set([iterable])
set_b=set([i for i in range(5)])
set_b=set(range(5))
set_b=set([0,1,2,3,4])
print(set_a)
print(set_b)

print('###---frozenset---###')
# frozenset([iterable])
frozenset_a=frozenset([i for i in range(5)])
frozenset_a=frozenset(range(5))
frozenset_a=frozenset([0,1,2,3,4])
print(frozenset_a)

print('###---operations of both set and frozenset---###')
# len(s)
print(len(set_a))
# x (not) in s
print(5 in frozenset_a)
print(0 in set_a)
# isdisjoint(other)
print(set_a.isdisjoint(set_b))
# issubset(other)
print(frozenset_a.issubset(set_b))
print(frozenset_a<=set_b)
print(frozenset_a<set_b)
# issuperset(other)
print(set_b.issuperset(frozenset_a))
print(set_b>=frozenset_a)
print(set_b>frozenset_a)
# union(others)
print(set_a.union(set_b))
print(set_a|set_b|frozenset_a)
# intersection(others)
print(set_a.intersection(set_b))
print(set_b&frozenset_a)
# difference(others): A - B,in A not in B
print(set_a.difference(set_b))
print(set_a-frozenset_a)
# symmetric_difference(other): A|B - A&B
print(set_b.symmetric_difference(set(range(3,8))))
print(set_a^{'Anthony','Anderson','Angela','Darrell','Kevin'})
# cpoy():shallow copy
copy_a=set_a.copy()
print(copy_a)
# euqal
# !!! instaces of set are compared to instances of frozenset based on their members
print(set_b==frozenset_a)
print(set_b in set([frozenset_a]))
print(set_b in set(frozenset_a))

print('###---operations of set---###')
# update(others)
set_c={0,1,2,3,4}
set_c.update(set_b)
set_c |={5,6,7,8,9} | {'Angela','Darrell','Kevin','Joey'}
print(set_c)
# intersection_update(others)
set_d=set([x for x in range(5)])
set_d.intersection_update(set_b)
set_d &=set_b &{3,4}
print(set_d)
# difference_update(others)
set_e=set(range(5))
set_e.difference_update({4})
set_e -= {3} | {2}
print(set_e)
# symmetric_difference_update(other)
set_f=set(range(5))
set_f.symmetric_difference_update(set(range(3,8)))
set_f ^= set(range(5,6))
print(set_f)

# add(elem)
set_a.add('Angela')
print(set_a)
# remove(elem)
set_a.remove('Angela')
print(set_a)
try:
	set_a.remove(5)
except KeyError:
	print('Can\'t remove element,KeyError')
# discard(elem)
set_a.discard(5)
# pop()
for i in range(4):
	print(set_a.pop())
try:
	set_a.pop()
except KeyError:
	print('Can\'t remove and return element when set is empty,KeyError')
# clear()
set_a.clear()
set_b.clear()
set_c.clear()
set_d.clear()
set_e.clear()
set_f.clear()