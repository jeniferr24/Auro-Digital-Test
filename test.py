f=open('orders.xml')
import heapq as h
books={}
while True:
    x=f.readline()
    if not x:
        break
    x=x.strip().split()
    if x[1] not in books:
        buy=[]
        sell=[]
        h.heapify(buy)
        h.heapify(sell)
        books[x[1]]=[buy,sell]
    if x[0]=='<AddOrder':
        if 'BUY' in x[2]:
            h.heappush(books[x[1]][0],[-int(x[3][8:-1]),int(x[4][9:])])
print(books)
            
        
