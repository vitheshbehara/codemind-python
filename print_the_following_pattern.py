n=int(input())
l="ZXCVBNMLKJHGFDSAQWERTYUIOP"
l=list(l)
l.sort()
for i in range(n):
    for j in range(n):
        print(l[i],end=" ")
    print()