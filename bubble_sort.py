import random

def new_num(lis):
    for i in range(50):
        j = random.randint(0,100000)
        lis.append(j)

l=[]
new_num(l)

def bubble_sort(list):
    for j in range(len(list)-1,0,-1):
        for i in range(j):
            if list[i] > list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]

bubble_sort(l)
for i in l:
    print(i)
