import random
a=[]
for i in range(10):
    a.append(random.randint(1,100))
a.sort()
print(a)

num=int(input("Input a num between 1 and 100:"))
a.append(num)

for i in range(10):
    if a[i] > num:
        t1=a[i]
        a[i]=num
        for j in range(i+1,11):
            t2=a[j]
            a[j]=t1
            t1=t2
        break
print("---------------")
print(a)

