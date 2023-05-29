import API_Grafos_2 as G

g1 = G.Grafo(8)

g1.addAresta(0, 1)
g1.addAresta(0, 7)
g1.addAresta(0, 6)
g1.addAresta(0, 5)
g1.addAresta(1, 7)
g1.addAresta(2, 3)
g1.addAresta(2, 5)
g1.addAresta(3, 4)
g1.addAresta(5, 6)
g1.addAresta(6, 8)

g1.mostrar_vertices()

'''dfs = G.BuscaEmProfundidade(g1, 4)
print(dfs.v_marcado(1))
print(dfs.contador())

bfs = G.BuscaEmLargura(g1, 2)
print(bfs.v_marcado(2))


print('\n')

g1.dijkstra(1)
# Acessar as distâncias mínimas e predecessores para cada vértice
for v in range(g1.V()):
    print(f"Distância mínima até o vértice {v}: {g1.d[v]}")
    print(f"Predecessor do vértice {v}: {g1.pi[v]}")
    print()


if g1.bellman_ford(4):
    print("Ciclo de peso negativo encontrado")
else:
    print("Não há ciclos de peso negativo")'''

g1.floyd_warshall();