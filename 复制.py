import copy
a=[1,2,3]
b=a
print(id(a))

c=copy.deepcopy(a)
print(id(c))
