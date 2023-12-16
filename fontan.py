n,m=map(int,input().split())
final_lst = []
for row in range(n):
    column = input()
    lst=[]
    if row == 0:
        for elem in column:
            lst.append(elem)
        
    else:
        for elem in column:
            lst.append(elem)
        for i in range(len(lst)):
            if lst[i] == '.':
                if final_lst[row-1][i] == 'V':
                    lst[i] = 'V'
            elif lst[i] == '#':
                if final_lst[row-1][i] == 'V':
                    if i == 0:
                        if i+1<len(lst):
                            if final_lst[row-1][i+1] == '.':
                                final_lst[row-1][i+1]='V'
                                if lst[i+1] == '.':
                                    lst[i+1]='V'
                    else:
                        for j in range(i,0,-1):
                            if lst[j] == '#':
                                if final_lst[row-1][j] == 'V':
                                    if j+1<len(lst):
                                        if final_lst[row-1][j+1] == '.':
                                            final_lst[row-1][j+1]='V'
                                            if lst[j+1] == '.':
                                                lst[j+1]='V'
                                    if j-1>=0:
                                        if final_lst[row-1][j-1] == '.':
                                            final_lst[row-1][j-1]='V'
                                            if lst[j-1]=='.':
                                                lst[j-1]='V'
                                
    final_lst.append(lst)
for elem in final_lst:
    print(''.join(elem))