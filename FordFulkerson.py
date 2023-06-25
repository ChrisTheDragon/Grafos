from collections import deque
from typing import List, Tuple


def ford_fulkerson(graph: List[List[int]], source: int, terminal: int) -> Tuple[int, List[List[int]]]:
    """
    Executa o algoritmo de Ford-Fulkerson para encontrar o fluxo máximo em um grafo.

    Args:
        graph (List[List[int]]): Matriz de adjacência do grafo.
        source (int): Vértice de origem.
        terminal (int): Vértice de destino.

    Returns:
        Tuple[int, List[List[int]]]: Fluxo máximo e o grafo residual resultante.
    """
    V = len(graph)
    rGraph = [[0] * V for _ in range(V)]

    # Cria uma cópia do grafo original
    for u in range(V):
        for v in range(V):
            rGraph[u][v] = graph[u][v]

    parent = [-1] * V
    max_flow = 0

    while bfs(rGraph, source, terminal, parent):
        # Encontra o valor do fluxo possível no caminho encontrado
        path_flow = float('inf')
        v = terminal
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, rGraph[u][v])
            v = parent[v]

        # Atualiza as capacidades residuais das arestas e das arestas reversas
        v = terminal
        while v != source:
            u = parent[v]
            rGraph[u][v] -= path_flow
            rGraph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow, rGraph


def bfs(rGraph: List[List[int]], source: int, terminal: int, parent: List[int]) -> bool:
    """
    Executa uma busca em largura (BFS) no grafo residual para encontrar um caminho aumentante.

    Args:
        rGraph (List[List[int]]): Grafo residual.
        source (int): Vértice de origem.
        terminal (int): Vértice de destino.
        parent (List[int]): Lista para armazenar o caminho encontrado.

    Returns:
        bool: True se houver um caminho aumentante, False caso contrário.
    """
    V = len(rGraph)
    visited = [False] * V
    queue = deque()
    queue.append(source)
    visited[source] = True
    parent[source] = -1

    while queue:
        u = queue.popleft()

        for v in range(V):
            if not visited[v] and rGraph[u][v] > 0:
                if v == terminal:
                    parent[v] = u
                    return True
                queue.append(v)
                parent[v] = u
                visited[v] = True

    return False


# Exemplo de uso
graph = [
    [0, 6, 12, 0, 0, 0], 
    [0, 0, 0, 8, 0, 0], 
    [0, 0, 0, 3, 5, 0], 
    [0, 0, 0, 0, 0, 7], 
    [0, 0, 0, 0, 0, 14],
    [0, 0, 0, 0, 0, 0], 
]

source = 0  # Vértice de origem
terminal = 5    # Vértice de destino

max_flow, residual_graph = ford_fulkerson(graph=graph, source=source, terminal=terminal)

print(f'Fluxo máximo: {max_flow}')
print('Grafo Residual:')
for row in residual_graph:
    print(row)
