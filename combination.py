def combination (n,r):
    if n<0 or r<0 or n==0 or n<r:
                print("combination is not possible")
    else:
                        fact1=1
                        for i in range(1,n+1):
                                fact1=fact1*i
                        fact2=1
                        for i in range(1,r+1):
                                fact2=fact2*i
                        fact3=1
                        for i in range(1,(n-r)+1):
                                fact3=fact3*i
    return(fact1/fact2*fact3)
