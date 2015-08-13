def create_graph(words):
    # build graph out of x 
    graph = {}
    levels = len(words)
    
    for level in range(levels-1):
        ##func edge
        edge = check_edge(words[level], words[level+1])
        if edge is not None: 
            node, points_to = edge
            if node in graph: 
                graph[node].append(points_to)
            else: 
                graph[node] = [points_to] 
    return graph


def check_edge(e1, e2):
    distance = min(len(e1), len(e2))
    for letter in range(distance):
        if e1[letter] != e2[letter]:
            return e1[letter], e2[letter]


def leftmost_nodes(graph):
    
    edges = [zip(*graph.values())]
    leftmost_nodes = {nodes for nodes in graph if nodes not in edges}
    return leftmost_nodes


def answer(words):
    graph = create_graph(words)
    roots = leftmost_nodes(graph)
    visited, alphabet = [], []

    def dfs(node):
      if node not in visited:
        visited.append(node)
        if node in graph:
          for edge in graph[node]:
            dfs(edge)
        alphabet.append(node)

    for node in roots:
      dfs(node)
       
    # concatenate a list and reverse it
    return ''.join(alphabet[::-1])

print answer(['ba', 'ab', 'cb'])
