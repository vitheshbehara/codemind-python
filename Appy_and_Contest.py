def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)
def lcm(a,b):
    if b>a:
        a,b = b,a
    return a*b//hcf(a,b)
t = int(input())
for _ in  range(t):
    n,a,b,k = map(int,input().split())
    x = n//a
    y = n//b
    z = n//(lcm(a,b))
    if (x+y-2*z >= k):
        print("Win")
    else:
        print("Lose")