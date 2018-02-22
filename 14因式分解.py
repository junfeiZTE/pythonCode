def reduceNum(n):
    print("%d =" % n,end='')
    while n not in [1]:
        for index in range(2,n+1):
            if n % index == 0:
                n //= index
                if n == 1:
                    print(" %d"%index)
                else:
                    print(" %d *"%index,end='')
                break

reduceNum(90)
reduceNum(100)
