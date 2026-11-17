def so_nguyen_to(a):
    if a<2:
        return False
    else:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
        return True

a=list(map(int, input('').split()))
count=0
tong=0
for i in range(len(a)):
    if so_nguyen_to(a[i]):
        print(a[i],end=' ')
        count+=1
        tong+=a[i]
if count==0:
    print('-')
else:
    print()
    print(tong)            