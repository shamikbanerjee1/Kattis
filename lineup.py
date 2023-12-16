lst=[]
for _ in range(int(input())):
    lst.append(input())
lst_inc=sorted(lst)
lst_dec=sorted(lst,reverse=True)
if lst==lst_inc:
    print('INCREASING')
elif lst==lst_dec:
    print('DECREASING')
else:
    print('NEITHER')