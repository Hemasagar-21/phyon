li=[3,3]
lis=[]
for i in range(0,len(li)):
    for j in range(1,len(li)):
        if(li[i]+li[j]==6):
            if i not in lis:
                lis.append(i)
                lis.append(j)
print(lis)
