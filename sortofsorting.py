n=int(input())
while n!=0:
    lst=[input() for _ in range(n)]
    lst.sort(key=lambda x:x[:2])
    for elem in lst:
        print(elem)
    print()
    n=int(input())