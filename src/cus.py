import heapq

class UCS:
    
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
    
    def search(self):
        """
        Searches for the least cost path from the start node to the goal node using Uniform Cost Search (UCS).
        
        Returns:
            A list of nodes representing the path from the start to the goal, or None if no path exists.
        """
        
        # frontier is a priority queue that holds tuples of (cost, node, path)
        frontier = []
        heapq.heappush(frontier, (0, self.start, [self.start])) # initialize the frontier with the start node, cost - 0, and path containing only the start node
        
        # Set to keep track of visited nodes
        visited = set() 
        
        while frontier:
            cost, node, path = heapq.heappop(frontier) # get the node with the lowest cost from the frontier
            if node in visited:
                continue # skip if the node has already been visited
            if node == self.goal:
                return cost, path # return the total cost and the path to the goal
            visited.add(node)
            
            # expand the node by adding its neighbors to the frontier with their respective costs
            for neighbor, edge_cost in self.graph.get(node, []):
                if neighbor not in visited:
                    new_cost = cost + edge_cost 
                    new_path = path + [neighbor]
                    heapq.heappush(frontier, (new_cost, neighbor, new_path))
                
        return "Caminho não encontrado"
    
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('D', 2)],
        'C': [('A', 4), ('D', 5)],
        'D': [('B', 2), ('C', 5)]
    }
    
    ucs = UCS(graph, 'A', 'D')
    result = ucs.search()
    print(result)