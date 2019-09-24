def isEven(n1):
    if n1%2==0:
        return True
    return False

def isOdd(n1):
    if n1%2!=0:
        return True
    return False  

def isPrime(n1):
    c=0
    for i in range(1,n1):
        if n1%i==0:
            c+=1
    if c==2:
        return True
    return False
  