a=2
b=1
s=0
for  n in range(1,21):
    s+=a/b
    a,b=a+b,a
print(s)
