'''


Aluno: Christian J. C. Marinho
Matricula: 202004940041
'''

class Grafos_Lista:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.lista_adjacencias = [[] for _ in range(num_vertices)]
    
    
    def V(self):
        return self.num_vertices
    
    
    def A(self):
        aresta = 0
        
        for row in self.lista_adjacencias:
            aresta += len(row)
        
        return aresta/2
    

    def AddAresta(self, origem: int, destino: int):
        # Verifica se a origem e o destino são válidos
        if destino > self.num_vertices or origem > self.num_vertices:
            print(f'ERRO: Aresta {origem, destino} fora do grafo\n')
        else:
            # Adiciona a aresta na lista de adjacências de ambas as direções
            self.lista_adjacencias[origem-1].append(destino)
            self.lista_adjacencias[destino-1].append(origem)
        
    
    def mostrar_vertices(self):
        # Percorre a lista de adjacências de cada vértice e imprime na tela
        for i in range(self.num_vertices):
            print(f"Vértice {i+1} -> ", end=" ")
            for j in self.lista_adjacencias[i]:
                print(j, end=" ")
            print()
        print()

    
    def Adj(self, vertice):
        #print(f'Adjacencias ao vertice {vertice}: {self.lista_adjacencias[vertice-1]}\n')
        return self.lista_adjacencias[vertice-1]





class Grafos_Matrizes:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        # Cria uma matriz de adjacências vazia com dimensão num_vertices x num_vertices
        self.matriz_adjacencias = [[0] * num_vertices for _ in range(num_vertices)]
        
    
    def V(self):
        return self.num_vertices
    

    def A(self):
        aresta = 0

        for i in range(self.num_vertices):
            for j in range(i+1, self.num_vertices):
                if self.matriz_adjacencias[i][j] != 0:
                    aresta += 1

        return aresta


    def AddAresta(self, origem: int, destino: int):
        # Verifica se a origem e o destino são válidos
        if destino > self.num_vertices or origem > self.num_vertices:
            print(f'ERRO: Aresta {origem, destino} fora do grafo\n')
        else:
            # Adiciona a aresta na lista de adjacências de ambas as direções
            self.matriz_adjacencias[origem-1][destino-1] = 1
            self.matriz_adjacencias[destino-1][origem-1] = 1
            

    def mostrar_vertices(self):
        # Percorre a matriz de adjacências e imprime na tela 1 para arestas e 0 para ausência de arestas
        print("    ", end="")
        for j in range(self.num_vertices):
            print(f"[{j+1}]", end="")
        print()
        
        for i in range(self.num_vertices):
            print(f'[{i+1}]', end=" ")
            for j in range(self.num_vertices):
                if self.matriz_adjacencias[i][j] != 0:
                    print(f' {1}', end=" ")
                else:
                    print(f' {0}', end=" ")
            print()
        print()
        
        
    def Adj(self, vertice: int):
        print(f'Adjacências ao vértice {vertice}:', end=" ")
        for i in range(self.num_vertices):
            if self.matriz_adjacencias[vertice-1][i] != 0:
                print(i+1, end=" ")
        print()




class BuscaEmProfundidade:
    def __init__(self, G: Grafos_Lista):
        self.pi = dict() #salva o antecessor de um vertice. Sempre que um vertice v for descoberto durante a leitura da lista de adj. de um vertice ja descoberto u, π[v] = u;
        self.cor = dict() #mantem a cor do vertice u e V
        self.__d = dict() #salva o tempo de quando o vertice v foi descoberto e colorido como cinza;
        self.__f = dict() #salva o tempo de quando de quando a busca finaliza o exame da lista de adjacencias do vertice v e o colore como preto.
        self.time = 0
        #self.marcado = []
        self.G = G


    def DFS(self):
        for vertice in range(self.G.num_vertices): 
            self.pi[vertice+1] = None #Iniciado com Nulo
            self.cor[vertice+1] = "BRANCO" #Inicializacao - vertices coloridos de branco;
        
        for vertice in range(self.G.num_vertices):
            if self.cor[vertice+1] == "BRANCO":
                self.dfs_visit(vertice+1)


    def dfs_visit(self, u):
        self.cor[u] = "CINZA"
        self.time = self.time + 1
        self.__d[u] = self.time

        #Explorar a aresta (u,v)
        for v in self.G.Adj(u):
            if self.cor[v] == "BRANCO":
                self.pi[v] = u #O antecessor de ’v’ = ’u’
                self.dfs_visit(v)
        
        self.cor[u] = "PRETO" #vertice ’u’ finalizado
        self.time = self.time+1
        self.__f[u] = self.time
        
    
    def marcado(self, w: int):
        return self.__f[w]
        
        
    def get_tempos_iniciais(self):
        return self.__d
    
    
    def get_tempos_finais(self):
        return self.__f
    
    
    def get_antecessores(self):
        return self.pi
    
    
    def print_resultado_DFS(self):
        print("Tempo de descoberta de cada vértice (d):")
        for v, tempo in self.__d.items():
            print(f"vértice {v}: {tempo}")
            
        print("\nTempo de término de cada vértice (f):")
        for v, tempo in self.__f.items():
            print(f"vértice {v}: {tempo}")
            
        print("\nLista de antecessores de cada vértice:")
        for v, antecessor in self.pi.items():
            if antecessor is None:
                print(f"vértice {v}: sem antecessor")
            else:
                print(f"vértice {v}: {antecessor}")