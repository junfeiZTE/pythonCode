import random

def new_num(lis):
    for i in range(50):
        j = random.randint(0,100000)
        lis.append(j)

l=[]
new_num(l)

def selection_sort(list):
    n=len(list)
    for j in range(n-1):
        min_index=j
        for i in range(j+1,n):
            if list[i] < list[min_index]:
                min_index=i
            if min_index!=j:
                list[j],list[min_index]=list[min_index],list[j]

selection_sort(l)
for i in l:
    print(i)
