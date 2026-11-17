a=list(map(int, input('').split()))
A=[]
dem=0
for i in range(len(a)):
    if a[i]<0:
        A.append(a[i])
        dem+=1
if dem==0:
    print('-')   
else:
    print(max(A))         