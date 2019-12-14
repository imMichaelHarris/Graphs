
"""



def get_neighbors(word):
    '''
    return all words from word_list that are 1 letter different
    '''
    # change one letter to another letter in the alphabet incrementally
    # search the graph for that
    # then repeat for each letter in the word
    neighbors = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # For each letter in the word,
    for i in range(len(word)):
        # For each letter in the alphabet
        for letter in alphabet:
            # Change the word letter to the alphabet letter
            list_word = list(word)
            list_word[i] = letter
            w = "".join(list_word)
            # If the new word is in the word_set:
            if w != word and w in word_set:
                # Add it to neighbors
                neighbors.append(w)
    return neighbors
​


Return the fartest which sounds like a depth first traversal but need to go up not down
"""

the_list = [(1,3), (2,3), (3,6), (5,6), (5,7), (4,5), (4,8), (8,9), (11,8), (10,1)]

def earliest_ancestor(ancestors, starting_node):
    # Do a DFT with the starting node for a start think might have to reverse it - hmmm if we only check if the node is the second item of tuple dft should be fine
    # Get neighbors of the starting node
    # Loop through and find the tuple(s) that have the starting node ad the second item
    # Use recursion to call this function again 
    # If the starting node has been visted move on
    # Base case will be when there is no tuple with the starting node in it's second index

    my_graph = Graph()

    for i in ancestors:
        my_graph.add_vertex(i[0])
        my_graph.add_vertex(i[1])
        my_graph.add_edge(i[1], i[0])

    q = Queue()
    q.enqueue([starting_node])
    
    while q.size() > 0:
        max_path = 1
        ancestor = -1
        path = q.dequeue()
        vertex = path[-1]
        if (len(path) >= max_path and vertex < ancestor) or (len(path) > max_path):
            ancestor = vertex
            max_path = len(path)
            

        for neighbor in my_graph.vertices[vertex]:
            new_path = list(v)
            new_path.append(neighbor)
            q.enqueue(new_path)
        
        return ancestor
            
    # print("start", starting_node, path, visited)
    # # visited.add(starting_node)
    # new_path = path + [starting_node]
    # print("paths", path, new_path)
    # if len(new_path) > max_path:
    #     # print("bigger")
    #     path = new_path
    #     max_path = len(new_path)
    # else:
    #     print("first else")
    #     return path
    # for i in range(len(ancestors)):
    #     # print(ancestors[i])
    #     if ancestors[i][1] == starting_node:
    #         # print("Found", ancestors[i][0], ancestors[i])
    #         if ancestors[i][1] not in visited:
    #         # path = list([ancestors[i]])
    #             # print("path",path)
    #             # path.append(ancestors[i][0])
    #             visited.add(ancestors[i][1])
    #             new_path = earliest_ancestor(ancestors, ancestors[i][0], visited, path)
    #             if new_path is None:
    #                 if max_path 
    #                 print("here", starting_node, "path: ", path, ancestors[i][0])
    #                 return
                    
    
                
            # else:
            #     print("else")
            #     return starting_node

        # print(starting_vertex)
    # for neightbor in self.get_neighbors(starting_vertex):
    #     if neightbor not in visited:
    #         self.dft_recursive(neightbor, visited)/

    
print(earliest_ancestor(the_list, 6))