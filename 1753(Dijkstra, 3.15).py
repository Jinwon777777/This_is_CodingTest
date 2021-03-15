import sys
import heapq as hq

input = sys.stdin.readline

v, e = map(int, input().split())

k = int(input())

INF = int(1e9)
#
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    distance[start] = 0
    hq.heappush(q, (0,start))
    while q:
        dis, node = hq.heappop(q)
        if distance[node] < dis:
            continue
        for i in graph[node]:
            cost = i[1]+dis
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(q, (cost, i[0]))

dijkstra(k)
for dis in distance[1:]:
    if dis == int(1e9):
        print('INF')
    else:
        print(dis)