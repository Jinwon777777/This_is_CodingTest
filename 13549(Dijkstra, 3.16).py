import heapq as hq
x,y = map(int, input().split())

visited = [False]*100001

h = []
hq.heappush(h, (0,x))

while h:
    sec, node = hq.heappop(h)
    if node <0 or node > 100000 or visited[node] == True:
        continue
    visited[node] = True
    if node == y:
        break
    if node < y:
        hq.heappush(h, (sec,2*node))
        hq.heappush(h,(sec+1, node-1))
        hq.heappush(h,(sec+1, node+1))
    else:
        hq.heappush(h,(sec+1, node-1))
            

print(sec)