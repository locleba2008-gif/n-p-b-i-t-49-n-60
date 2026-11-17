def so_nguyen_to(n):
    if n<2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

a=list(map(int, input('').split()))
dem=0
A=[]
for i in range (len(a)):
    if so_nguyen_to(a[i]):
        dem+=1
        A.append(a[i])  
if dem==0:
    print('-')
else:
    print(max(A))                  