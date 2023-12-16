s = set()
line_number=0
flag=True
for _ in range(int(input())):
    ip=input().split()
    line_number+=1
    if ip[0] != '->':
        if len(s)==0:
            flag=False
            break
        else:
            index_br = ip.index('->')
            for i in range(index_br):
                if ip[i] not in s:
                    flag=False
                    break
            if flag:
                s.add(ip[index_br+1])
        if not flag:
            break
    else:
        s.add(ip[1])
if flag:
    print('correct')
else:
    print(line_number)