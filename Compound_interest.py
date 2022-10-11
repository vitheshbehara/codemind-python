p,r,t=list(map(int,input().split()))
compound_interest=(p*((1+r/100)**t))
print("%0.2f"%compound_interest)