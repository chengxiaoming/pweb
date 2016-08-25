print('aaa')
a = input()
print(a)

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

print(power(2,3))
