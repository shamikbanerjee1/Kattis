dic={}
for i in range(int(input())):
    ip=input().split()
    country,yr=ip[0],int(ip[1])
    if dic.get(country):
        dic[country].append(yr)
    else:
        dic[country]=[yr]
for k,v in dic.items():
    v.sort()
for _ in range(int(input())):
    query=input().split()
    print(dic[query[0]][int(query[1])-1])