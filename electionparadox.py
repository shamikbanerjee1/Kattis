regions = int(input())
list_votes = list(map(int,input().split()))
list_votes.sort(reverse=True)
max_votes = 0
full_votes_from = regions//2
for i in range(full_votes_from):
    max_votes += list_votes[i]
for i in range(full_votes_from,len(list_votes)):
    max_votes += list_votes[i]//2
print(max_votes)