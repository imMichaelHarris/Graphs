"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.cache = set()

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enquese the starting vertex id
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an empty set to store visited vertices
        visited = set()
        # While the queue is not empty 
        print("BFT")
        while q.size() > 0:
        #   dequeue the first vertex
            v = q.dequeue()
        #   If that vertex hasn't been visited..
            if v not in visited:
                print(v)
        #       Mark as visited
                visited.add(v)
        #       Then add all of it's neighbors to back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

 
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        # Create an empty set to store visited vertices
        visited = set()
        print("DFT")
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.vertices[v]:
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Make base case - return when starting_vertex is already in cache
        if starting_vertex in self.cache:
            return  
        print(starting_vertex)
        for neightbor in self.vertices[starting_vertex]:
            self.cache.add(starting_vertex)
            self.dft_recursive(neightbor)

        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        print("BFS")
        while q.size() > 0:
            v = q.dequeue()
            vertex = v[-1]
            if vertex not in visited:
                if vertex is destination_vertex:
                    return v
                visited.add(vertex)
            for neighbor in self.vertices[vertex]:
                new_path = list(v)
                new_path.append(neighbor)
                q.enqueue(new_path)
            


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        # Create an empty set to store visited vertices
        visited = set()
        print("DFS")
        while s.size() > 0:
            v = s.pop()
            vertex = v[-1]
            if vertex not in visited:
                if vertex is destination_vertex:
                    return v
                visited.add(vertex)
            for neighbor in self.vertices[vertex]:
                new_path = list(v)
                new_path.append(neighbor)
                s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print("DFS RECURSION")
        if starting_vertex in self.cache:
            return  
        vertex = starting_vertex[-1]
        if starting_vertex is destination_vertex:
            return starting_vertex
        print(vertex)
        self.cache.add(vertex)
        for neightbor in self.vertices[vertex]:
            new_path = list(starting_vertex)
            new_path.append(neightbor)
            self.dft_recursive(new_path)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("DFT RECURSIVE")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
