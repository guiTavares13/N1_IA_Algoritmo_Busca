import heapq

def dijkstra(grafo, origem):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[origem] = 0
    heap = [(0, origem)]
    
    while heap:
        (dist, vertice) = heapq.heappop(heap)
        if dist > distancias[vertice]:
            continue
        
        for adjacente, custo in grafo[vertice].items():
            nova_distancia = dist + custo
            if nova_distancia < distancias[adjacente]:
                distancias[adjacente] = nova_distancia
                heapq.heappush(heap, (nova_distancia, adjacente))
    
    return distancias