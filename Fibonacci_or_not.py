n=int(input())
firstnumber=0
secondnumber=1
nextnumber=0
if n==1 or n==1:
    print(True)
else:
    c=0
    while nextnumber<=n:
        nextnumber=firstnumber+secondnumber
        firstnumber=secondnumber
        secondnumber=nextnumber
        if secondnumber==n:
            c+=1
            break
    if c==0:
        print(False)
    else:
        print(True)