n=int(input())
DOM=[]
kattis=[]
for i in range(2*n):
    if i < n:
        DOM.append(input())
    else:
        kattis.append(input())
DOM.sort()
kattis.sort()
max_val=0
i,j = 0,0
while i<n and j<n:
    if i==n or j==n:
        break
    if DOM[i]==kattis[j]:
        max_val+=1
        i+=1
        j+=1
    elif DOM[i]>kattis[j]:
        j+=1
    else:
        i+=1
print(max_val)
    