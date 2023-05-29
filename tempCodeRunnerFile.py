    if __init__ == '__main__':
        g1 = Grafo(8)

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