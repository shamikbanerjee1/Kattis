dic={}
for _ in range(int(input())):
    i = int(input())
    if not dic.get(i):
        print(i)
        dic[i] = [i]
    
    else:
        search_number=dic[i][-1]+i
        while dic.get(search_number):
            dic[i].append(search_number)
            search_number+=i
        print(search_number)
        dic[search_number]=[search_number]
        
                