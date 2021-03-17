import sys
import heapq as hq

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF] * (n + 1)
visited = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())


def dijkstra(start):
    q = []
    distance[start] = 0
    hq.heappush(q, (0, start, [start]))
    while q:
        dis, node, lis = hq.heappop(q)
        if distance[node] < dis:
            continue
        for i in graph[node]:
            cost = i[1]+dis
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                route = lis+[i[0]]
                visited[i[0]] = route
                hq.heappush(q, (cost, i[0], route))


dijkstra(start)
print(distance[end])
print(len(visited[end]))

for city in visited[end]:
    print(city, end=' ')
