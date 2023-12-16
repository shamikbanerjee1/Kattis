import heapq
class B:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
n,m,k=map(int,input().split())
unread_books=[]
b = B('Jane Eyre',k)
heapq.heappush(unread_books,(b.title, b.pages))
for _ in range(n):
    ip=input().split()
    pages=int(ip.pop())
    title = ' '.join(ip)
    title=title.strip('"')
    b = B(title,pages)
    heapq.heappush(unread_books, (b.title, b.pages))
incoming_books=[]
for _ in range(m):
    ip=input().split()
    time=int(ip.pop(0))
    pages=int(ip.pop())
    title=' '.join(ip)
    title=title.strip('"')
    b = B(title,pages)
    heapq.heappush(incoming_books,(time,b.title,b.pages))

current_book = heapq.heappop(unread_books)
start_time = current_book[1]
while current_book[0] != 'Jane Eyre':
    while incoming_books and start_time >= incoming_books[0][0]:
        heapq.heappush(unread_books,(incoming_books[0][1], incoming_books[0][2]))
        in_book=heapq.heappop(incoming_books)
    current_book = heapq.heappop(unread_books)
    start_time+=current_book[1]
print(start_time)