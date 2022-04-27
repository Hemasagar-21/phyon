n=int(input())
for i in range(n+1):
    for j in range(i):
        print('*',end=' ')
    print('\n')
for k in range(n-1,0,-1):
    for j in range(k):
        print('*',end=' ')
    print('\n')
