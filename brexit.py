from collections import defaultdict
import sys
from queue import PriorityQueue
c,p,x,l=map(int,sys.stdin.readline().split())
partnerships = defaultdict(set)
for _ in range(p):
    c1,c2=map(int,sys.stdin.readline().split())
    partnerships[c1].add(c2)
    partnerships[c2].add(c1)
frequency=defaultdict(lambda:0)
for key,value in partnerships.items():
    frequency[key] += len(value)
if l == x:
    print('leave')
else:
    leaving_members = PriorityQueue()
    leaving_members.put(l)
    while not leaving_members.empty():
        leaving_country = leaving_members.get()
        for partner in partnerships[leaving_country]:
            partnerships[partner].discard(leaving_country)
            rem_partner_length= len(partnerships[partner])
            if ((rem_partner_length/frequency[partner])*100 <= 50.0):
                leaving_members.put(partner)
        del partnerships[leaving_country]
    if (((len(partnerships[x]))/frequency[x])*100 >= 50.0):
        print('stay')
    else:
        print('leave')
