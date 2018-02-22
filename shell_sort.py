import random

def new_num(lis):
    for i in range(50):
        j = random.randint(0,100000)
        lis.append(j)

l=[]
new_num(l)

def shell_sort(list):
    n=len(list)
    gap=n//2

    while gap > 0:
        for j in range(gap,n):
            i=j
            while i>=gap and list[i-gap]>list[i]:
                list[i-gap],list[i]=list[i],list[i-gap]
                i-=gap
        gap//=2

shell_sort(l)

for i in l:
    print(i)
