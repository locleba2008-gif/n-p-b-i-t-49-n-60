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
if len(A)<3:
    print('-')
else:                 
    for k in range(len(A)-1):
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]            
    print(A[len(A)-3])                
