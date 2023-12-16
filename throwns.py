n,k=map(int,input().split())
commands=input().split()
lst=[]
i=0
indx_tracker=0
lst.append(indx_tracker)
while i<len(commands):
    try:
        indx=int(commands[i])
        indx_tracker = (indx_tracker+indx)%n
        
        if indx_tracker<0:
            indx_tracker = n+indx_tracker
        lst.append(indx_tracker)
        i+=1
    except:
        freq=int(commands[i+1])
        while freq!=0:
            lst.pop()
            freq-=1
        indx_tracker=lst[-1]
        i+=2
print(indx_tracker)    
