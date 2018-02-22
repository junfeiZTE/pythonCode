import random

def new_num(lis):
    for i in range(50):
        j = random.randint(0,100000)
        lis.append(j)

l=[]
new_num(l)

def insert_sort(list):
    n=len(list)
    for j in range(1,n):
        for i in range(j,0,-1):
            if list[i]<list[i-1]:
                list[i],list[i-1]=list[i-1],list[i]

insert_sort(l)
for i in l:
    print(i)
