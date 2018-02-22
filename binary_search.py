lis=[1,2,3,4,6,7,8,9,10,12,14]

def bin_search(list,item):
    print(list)
    if len(list) == 0:
        return False

    else:
        midpoint=len(list)//2

        if list[midpoint]==item:
            return True
        else:
            if list[midpoint]>item:
                return bin_search(list[:midpoint],item)
            else:
                return bin_search(list[midpoint:],item)

if bin_search(lis,6):
    print("Found!")
else:
    print("Not found!!")
