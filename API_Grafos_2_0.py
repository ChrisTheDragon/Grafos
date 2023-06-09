'''
Trabalho 10 - Implementar o Alg. de Warshall para encontrar o Fecho Transitivo
Baseado em uma representação computacional de grafos implementada anteriormente, implementar o Alg. de Warshall para encontrar o Fecho Transitivo.

Aluno: Christian J. C. Marinho
Matricula: 202004940041
'''

from collections import deque
import heapq
import random

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
        self.d = [float('inf')] * num_vertices
        self.pi = [None] * num_vertices
    
    def V(self):
        return self.num_vertices
    
    def A(self):
        aresta = 0
        
        for row in self.adj_list:
            aresta += len(row)
        
        return aresta/2
    
    def d_minima(self, v):
        return self.d[v]
    
    def addAresta(self, v, w):
        # Verifica se a origem e o destino são válidos
        if v >= self.num_vertices or w >= self.num_vertices:
            print(f'ERRO: Aresta {v, w} fora do grafo\n')
        else:
            # Adiciona a aresta na lista de adjacências de ambas as direções
            self.adj_list[v].append(w)
            self.adj_list[w].append(v)
    
    def adj(self, v):
        return self.adj_list[v]
    
    def mostrar_vertices(self):
        # Percorre a lista de adjacências de cada vértice e imprime na tela
        for i in range(self.num_vertices):
            print(f"Vértice {i} -> ", end=" ")
            for j in self.adj_list[i]:
                print(j, end=" ")
            print()
        print()
           
    def initialize_single_source(self, s):
        for v in range(self.V()):
            self.d[v] = float('inf')
            self.pi[v] = None
        self.d[s] = 0
    
    def relax(self, u, v, w):
        if self.d[v] > self.d[u] + w:
            self.d[v] = self.d[u] + w
            self.pi[v] = u
    
    def weight(self):
        return random.randint(1, 5)
    
    def dijkstra(self, s):
        self.initialize_single_source(s)
        S = set()
        Q = []
        heapq.heappush(Q, (0, s))

        while Q:
            _, u = heapq.heappop(Q)
            S.add(u)

            for v in self.adj(u):
                self.relax(u, v, self.weight())
                if v not in S:
                    heapq.heappush(Q, (self.d[v], v))
                    
    def bellman_ford(self, s):
        self.initialize_single_source(s)
        
        for _ in range(self.V() - 1):
            for u in range(self.V()):
                for v in self.adj(u):
                    self.relax(u, v, self.weight())
        
        for u in range(self.V()):
            for v in self.adj(u):
                if self.d[v] > self.d[u] + self.weight():
                    return True
        
        return False
    
    def floyd_warshall(self):
        n = self.V()
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        pred = [[None for _ in range(n)] for _ in range(n)]
        
        for v in range(n):
            for w in range(n):
                if v == w:
                    dist[v][w] = 0
                else:
                    for u in self.adj(v):
                        if u == w:
                            dist[v][w] = self.weight()
                    pred[v][w] = v
        
        for k in range(n):
            for v in range(n):
                for w in range(n):
                    if dist[v][k] + dist[k][w] < dist[v][w]:
                        dist[v][w] = dist[v][k] + dist[k][w]
                        pred[v][w] = pred[k][w]
        
        self.dist = dist
        self.pi = pred
        
        print("Matriz de distâncias:")
        for row in self.dist:
            print(row)
        
        print("\nMatriz de predecessores:")
        for row in self.pi:
            print(row)
    
    def warshall(self):
        n = self.V()
        fecho = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in self.adj(i):
                fecho[i][j] = 1
                
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    fecho[i][j] = fecho[i][j] or (fecho[i][k] and fecho[k][j])
        
        print("Fecho Transitivo:")
        for row in fecho:
            print(row)





class BuscaEmProfundidade:
    def __init__(self, G: Grafo, s):
        self.marcado = [False] * G.V()
        self.cont = 0
        self.dfs(G, s)
    
    def dfs(self, G: Grafo, v):
        self.marcado[v] = True
        self.cont += 1
        for w in G.adj(v):
            if not self.marcado[w]:
                self.dfs(G, w)
    
    def v_marcado(self, w):
        return self.marcado[w]
    
    def contador(self):
        return self.cont



class BuscaEmLargura:
    def __init__(self, G: Grafo, s):
        self.marcado = [False] * G.V()
        self.bfs(G, s)
    
    def bfs(self, G: Grafo, s):
        queue = deque()
        self.marcado[s] = True
        queue.append(s)
        while queue:
            v = queue.popleft()
            for w in G.adj(v):
                if not self.marcado[w]:
                    self.marcado[w] = True
                    queue.append(w)
    
    def v_marcado(self, w):
        return self.marcado[w]




class ComponentesConectados:
    def __init__(self, G: Grafo):
        self.marcado = [False] * G.V()
        self.componentes = []
        for v in range(G.V()):
            if not self.marcado[v]:
                componente = []
                self.dfs(G, v, componente)
                self.componentes.append(componente)
    
    def dfs(self, G: Grafo, v, componente):
        self.marcado[v] = True
        componente.append(v)
        for w in G.adj(v):
            if not self.marcado[w]:
                self.dfs(G, w, componente)
    
    def obter_componentes(self):
        return self.componentes
