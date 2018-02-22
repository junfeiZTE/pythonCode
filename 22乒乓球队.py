l = ['x','y','z']
for i in l:
    for j in l:
        for k in l:
            if i!=j and j!=k and k!=i:
                if i!= 'x' and k!= 'x' and k!='z':
                    print("order is a -- %c  b -- %c c -- %c"%(i,j,k))
                    
