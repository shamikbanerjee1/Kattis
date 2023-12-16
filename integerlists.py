from collections import deque
for _ in range(int(input())):
    command=input()
    flag=True
    n=int(input())
    x=input()
    err_flag=False
    x_lst=[]
    if n==0:
        x_lst=[]
    else:
        x_lst=x[1:len(x)-1].split(',')
    x_lst=deque(x_lst)
    for p in command:
        if p=='R':
            if flag:
                flag=False
            else:
                flag=True
        if p=='D':
            if len(x_lst)==0:
                err_flag=True
                break
            if flag:
                x_lst.popleft()
            else:
                x_lst.pop()
    if err_flag:
        print('error')
    else:
        if flag:
            print('[' + ','.join(x_lst) + ']')
        else:
            x_lst.reverse()
            print('[' + ','.join(x_lst) + ']')
            