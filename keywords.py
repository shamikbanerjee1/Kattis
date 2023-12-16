s=set()
for _ in range(int(input())):
    ip=input()
    ip = ip.lower()
    ip = ip.replace('-',' ')
    s.add(ip)
print(len(s))