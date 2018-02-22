N=10
print("Input 10 num:")
l=[]
for i in range(N):
    l.append(int(input("Input a num:")))
print("----------------")

for i in l:
    print(i)

for i in range(N-1):
    min=i
    for j in range(i+1,N):
        if l[min]>l[j]:
            min=j
        l[i],l[min]=l[min],l[i]

print("After sort")

for i in l:
    print(i)
