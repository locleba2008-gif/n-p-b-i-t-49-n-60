a=[]
n=int(input(''))
while True:
    line=input('').strip()
    if not line:
        break
    a.append(int(line))
A=[]
for x in a:
    if x not in A:
        A.append(x)
for x in A:
    print(f'{x}',f'{a.count(x)}',sep=' ')            