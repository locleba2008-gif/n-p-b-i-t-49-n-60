n=int(input(''))
a=[]
while True:
    line=input('').strip()
    if not line:
        break
    a.append(int(line))
A=[]
for x in a:
    if x not in A:
        A.append(x)
DEM=[]        
for i in range(len(A)):
    DEM.append(a.count(A[i]))
slxhnh=max(DEM)
for i in range(len(A)):
    if slxhnh==DEM[i]:
        print(A[i],end=' ')
print(slxhnh)        
    
    
