print('aaa')
a = input()
print(a)

from collections import Iterable
from collections import Iterator
def fil(x):
	return x%2 == 1
print(list(filter(fil,[1,2,3,4,5,6,7,8,9,0])))
print(sorted([9,-3,-10,8],key=abs,reverse=True))

def jj():
	for i in range(1,11):
		yield(i)
def add(x):
	return x*x
def fn(x,y):
	return x+y
fd = jj()
from functools import reduce
print(list(map(add,[1,5,6])),reduce(fn,[1,2,3,4,5]),fd)


print(ii,isinstance([],Iterable),isinstance([],Iterator))

from collections import Iterator
from collections import Iterable

print(isinstance([],Iterable),isinstance((x for x in range(1,3)),Iterator))


names = ['bob','michael']
names.append('cc')
bc = ('dd','ee')
print(names,names[0],bc,bc[1])
av = 0
if av > 0:
	print('if in')
else:
	print('if out')


for i in names:
	print(i)

dic = {'a':'aa','b':'bb'}
se = set(['h','h','g','y'])
print(dic,se)

def power(x,n):
	y = x*n
	return y

print(power(2,3),names[0:1])

print(list(range(1,11)))
print([x*x for x in range(1,10) if x%2 == 0])
print([x+y for x in "xyz" for y in "xyz"])


an = (x*x for x in range(1,10))
print(next(an),next(an),next(an))
for i in an:
	print('nnn',i)
