dic={}
level=0
for i in range(int(input())):
    lst=input().split()
    if lst[0] == 'TYPEOF':
        if dic.get(level):
            if dic[level].get(lst[1]):
                print(dic[level][lst[1]])
            else:
                flag=False
                temp=level
                while temp>=0:
                    temp-=1
                    if dic.get(temp):
                        if dic[temp].get(lst[1]):
                            flag=True
                            break
                if flag:
                    print(dic[temp][lst[1]])
                else:
                    print('UNDECLARED')
        else:
            flag=False
            temp=level
            while temp>=0:
                temp-=1
                if dic.get(temp):
                    if dic[temp].get(lst[1]):
                        flag=True
                        break
            if flag:
                print(dic[temp][lst[1]])
            else:
                print('UNDECLARED')
    elif lst[0] == 'DECLARE':
        if dic.get(level):
            if dic[level].get(lst[1]):
                print('MULTIPLE DECLARATION')
                break
            else:
                dic[level][lst[1]]=lst[2]
                
        else:
            dic[level] = {}
            dic[level][lst[1]] = lst[2]
            
    elif lst[0] == '{':
        level += 1
        dic[level]={}
      
    else:
        y = level
        del dic[level]
        level=y-1

    