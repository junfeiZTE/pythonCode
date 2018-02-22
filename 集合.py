list=('a','a','b','c','c')
print(set(list))

s="Welcome to the linux"
print(set(s))
uni=set(s)
uni.add('A')
print(uni)
uni.remove('x')
print(uni)
uni.discard('n')
print(uni)
#uni.clear()

uni1=set('linux')
print(uni.difference(uni1))
print(uni.intersection(uni1))

