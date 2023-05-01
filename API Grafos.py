
class Grafos_Lista:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista_adjacencias = [[] for _ in range(num_vertices)]
    
    
    def V(self):
        return self.num_vertices
    
    
    def A(self):
        aresta = 0
        
        for row in self.lista_adjacencias:
            aresta += len(row)
        
        return aresta/2
    

    def AddAresta(self, origem, destino):
        if destino > self.num_vertices or origem > self.num_vertices:
            print(f'ERRO: Aresta {origem, destino} fora do grafo\n')
        else:
            self.lista_adjacencias[origem-1].append(destino)
            self.lista_adjacencias[destino-1].append(origem)
        
    
    def mostrar_vertices(self):
        for i in range(self.num_vertices):
            print(f"Vértice {i+1} -> ", end=" ")
            for j in self.lista_adjacencias[i]:
                print(j, end=" ")
            print()
        print()

    
    def Adj(self, vertice):
        print(f'Adjacencias ao vertice {vertice}: {self.lista_adjacencias[vertice-1]}\n')


class Grafos_Matrizes:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
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


    def AddAresta(self, origem, destino):
        if destino > self.num_vertices or origem > self.num_vertices:
            print(f'ERRO: Aresta {origem, destino} fora do grafo\n')
        else:
            self.matriz_adjacencias[origem-1][destino-1] = 1
            self.matriz_adjacencias[destino-1][origem-1] = 1
            

    def mostrar_vertices(self):
        
        print("    ", end="")
        for j in range(self.num_vertices):
            print(f"[{j+1}]", end="")
        print()
        
        for i in range(self.num_vertices):
            #print(f"Vértice {i+1}:", end=" ")
            print(f'[{i+1}]', end=" ")
            for j in range(self.num_vertices):
                if self.matriz_adjacencias[i][j] != 0:
                    print(f' {1}', end=" ")
                else:
                    print(f' {0}', end=" ")
            print()
        print()
        
        
    def Adj(self, vertice):
        print(f'Adjacências ao vértice {vertice}:', end=" ")
        for i in range(self.num_vertices):
            if self.matriz_adjacencias[vertice-1][i] != 0:
                print(i+1, end=" ")
        print()



if __name__ ==  '__main__':
    # Teste da implementação de lista de adjacências
    g1 = Grafos_Lista(6)
    g1.AddAresta(1, 2)
    g1.AddAresta(1, 4)
    g1.AddAresta(2, 2)
    g1.AddAresta(2, 3)
    g1.AddAresta(2, 4)
    g1.AddAresta(3, 4)
    g1.AddAresta(4, 5)
    g1.AddAresta(5, 6)
    g1.AddAresta(6, 7)

    g1.mostrar_vertices()

    g2 = Grafos_Matrizes(6)
    g2.AddAresta(1, 2)
    g2.AddAresta(1, 4)
    g2.AddAresta(2, 2)
    g2.AddAresta(2, 3)
    g2.AddAresta(2, 4)
    g2.AddAresta(3, 4)
    g2.AddAresta(4, 5)
    g2.AddAresta(5, 6)
    g2.AddAresta(6, 7)

    g2.mostrar_vertices()
