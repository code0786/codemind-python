n=int(input())
sqn=n*n
rev=0
while n:
    rev=rev*10+n%10
    n//=10
sqrev=rev*rev
adam=0
while sqrev:
    adam=adam*10+sqrev%10
    sqrev//=10
if adam==sqn:
    print(True)
else:
    print(False)