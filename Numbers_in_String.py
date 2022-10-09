s=input()
a=[]
t="123456789"
for i in s:
    if i in t:
        a.append(int(i))
#print(a)
print(sum(a))
