import heapq

class UCS:
    
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
    
    def search(self):
        """
        Busca pelo caminho de menor custo do nó inicial ao nó objetivo usando a busca de custo uniforme (UCS).
        
        Returns:
            Uma lista de nós representando o caminho do início ao objetivo, ou None se nenhum caminho existir.
        """
        
        # frontier é uma fila de prioridade que contém tuplas de (custo, nó, caminho)
        frontier = []
        heapq.heappush(frontier, (0, self.start, [self.start])) # adicionar o nó inicial à fronteira com custo 0 e caminho contendo apenas o nó inicial
        
        # conjunto de nós visitados
        visited = set() 
        
        while frontier:
            cost, node, path = heapq.heappop(frontier) # pop o nó com o menor custo da fronteira
            if node in visited:
                continue # ignora se o nó já foi visitado
            if node == self.goal:
                return cost, path # retorna o custo total e o caminho encontrado se o nó objetivo for alcançado
            visited.add(node)
            
            # explora os vizinhos do nó atual e adiciona à fronteira se ainda não foram visitadoss
            for neighbor, edge_cost in self.graph.get(node, []):
                if neighbor not in visited:
                    new_cost = cost + edge_cost 
                    new_path = path + [neighbor]
                    heapq.heappush(frontier, (new_cost, neighbor, new_path))
                
        return "Caminho não encontrado"
    
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('E', 3)],
        'D': [('B', 5), ('E', 1)],
        'E': [('C', 3), ('D', 1)]
    }
    
    inicio = 'A'
    objetivo = 'E'
        
    ucs = UCS(graph, inicio, objetivo)
    resultado = ucs.search()
    
    if isinstance(resultado, tuple):
        custo, caminho = resultado
        print(f"Custo total: {custo}")
        print(f"Caminho encontrado: {' -> '.join(caminho)}")
    else:
        print(resultado)