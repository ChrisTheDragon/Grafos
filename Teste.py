import API_Grafos_1_5 as G

if __name__ ==  '__main__':
    # Teste da implementação de lista de adjacências
    g1 = G.Grafos_Lista(6)
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

    g2 = G.Grafos_Matrizes(6)
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
    
    
    dfs1 = G.BuscaEmProfundidade(g1)
    dfs1.DFS()
    dfs1.print_resultado_DFS()