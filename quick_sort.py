import random

def new_num(lis):
    for i in range(50):
        j = random.randint(0,100000)
        lis.append(j)

l=[]
new_num(l)

def quick_sort(list,start,end):
    if start>=end:
        return
    low=start
    high=end
    mid_value=list[low]

    while low < high:
        while low<high and list[high]>mid_value:
            high-=1

        list[low]=list[high]

        while high>low and list[low]<mid_value:
            low+=1

        list[high]=list[low]

    list[low]=mid_value

    quick_sort(list,start,low-1)
    quick_sort(list,high+1,end)

quick_sort(l,0,len(l)-1)

for i in l:
    print(i)

        
