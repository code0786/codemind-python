n=int(input())
sqn=n*n
sum=0
while sqn:
    sum+=sqn%10
    sqn//=10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")