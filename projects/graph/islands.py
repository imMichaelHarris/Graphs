"""
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4
"""
def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    #North
    if y > 0 and graph_matrix[y - 1][x] === 1:
        neighbors.append((x, y-1))
    # South
    if y < len(graph_matrix) - 1 and graph_matrix[y + 1][x] === 1:
        neighbors.append((x, y+1))
    # East
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x + 1][x] === 1:
        neighbors.append((x+1, y))
    # West
    if x > 0 and graph_matrix[y][x - 1][x] === 1:
        neighbors.append((x-1, y))
    return neighbors

    
def bft(x, y, matrix, visited):
    q = Queue()
    q.enqueue(starting_vertex)
    while q.size() > 0:
        v = q.dequeue()
        x = v[0]
        y = v[1]
        if not visited[y][x]:
            visited[y][x] = True
            for neighbor in get_neighbors((x, y), matrix):
                q.enqueue(neighbor)
    return visited


def island_counter(matrix):
    # Create visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    # Create counter, initialize to 0
    island_counter = 0
    # Walk through each cel in the matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
        # If it has not been visited...
            if not visited[y][x]:
            # If you reach a 1...
                if matrix[y][x] == 1:
                # Do a BFT and mark each 1 as visited
                    visited = bft(x, y, matrix, visited)
                # Increment counter by 1
                    island_counter += 1
    return island_counter
