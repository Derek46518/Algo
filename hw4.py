import heapq

def dijkstra(n, edges, source):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))
    
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[source] = 0
    pq = [(0, source)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            distance = current_dist + weight
            
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(pq, (distance, v))
    
    return dist

def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        
        m = int(input().strip())
        source = int(input().strip())
        
        edges = []
        for _ in range(m):
            u, v, w = map(int, input().strip().split())
            edges.append((u, v, w))
        
        distances = dijkstra(n, edges, source)
        
        for i in range(1, n + 1):
            if i != source:
                print(f"{source} to {i} = {distances[i]}")
        print()

if __name__ == "__main__":
    main()