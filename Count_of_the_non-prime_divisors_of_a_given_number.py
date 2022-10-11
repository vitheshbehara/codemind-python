def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
c=0
n=int(input())
for i in range(1,n+1):
    if n%i==0 and prime(i)==False:
        c=c+1
print(c)