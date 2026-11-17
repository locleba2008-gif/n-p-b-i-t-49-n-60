a=list(map(int, input('').split()))
A=[]
for x in a:
    if x not in A:
        A.append(x)
if len(A)<2:
    print('-')
else:                
    for k in range(len(A)-1):
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]            
    print(A[len(A)-2])            