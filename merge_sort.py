import random

def new_num(lis):
    for i in range(50):
        j = random.randint(0,100000)
        lis.append(j)

l=[]
new_num(l)

def merge_sort(list):
    n=len(list)
    if n<=1:
        return list
    mid = n//2

    left_list=merge_sort(list[:mid])
    right_list=merge_sort(list[mid:])

    left_pointer,right_pointer=0,0

    result=[]

    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] <= right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer+=1
        else:
            result.append(right_list[right_pointer])
            right_pointer+=1

    result+=left_list[left_pointer:]
    result+=right_list[right_pointer:]

    return result
        

l_r=merge_sort(l)

for i in l_r:
    print(i)
