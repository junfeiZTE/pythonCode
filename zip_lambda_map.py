a=[1,2,3]
b=[4,5,6]
print(list(zip(a,b)))

fun=lambda x,y:x+y
print(fun(1,2))

print(list(map(fun,[1,2,3],[4,5,6])))
