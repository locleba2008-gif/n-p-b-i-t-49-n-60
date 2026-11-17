def so_chinh_phuong(n):
    if n<0:
        return False
    else:
        if n!=(int(n**0.5))**2:
            return False
        return True
a=list(map(int, input('').split()))
count=0
tong=0
for i in range(len(a)):
    if so_chinh_phuong(a[i]):
        count+=1
        tong+=a[i]
if count==0:
    print('-')
else:
    TBC=tong/count
    print(f'{TBC:.1f}')            