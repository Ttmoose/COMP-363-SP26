def reachability(s: int, G: list[list[int]]) -> list:
    """
    Find all vertices in a graph G reachable from vertex s.

    Parameters:
    s (int): The starting vertex.
    G (list[list[int]]): The adjacency matrix representing the graph.

    Returns:
    list: A list of all vertices reachable from vertex s.
    """
    def dfs(v, visited):
        # Mark the current vertex as visited
        visited[v] = True
        reachable.append(v)
        
        # Explore all neighbors of the current vertex
        for neighbor, is_edge in enumerate(G[v]):
            if is_edge and not visited[neighbor]:  # If there's an edge and the neighbor is not visited
                dfs(neighbor, visited)

    # Initialize visited list and reachable list
    visited = [False] * len(G)
    reachable = []

    # Start DFS from vertex s
    dfs(s, visited)

    return reachable


# Test the function with the given adjacency matrix
graph = [
    # 0  1  2  3  4  5  6  7
    [ 0, 0, 0, 1, 0, 0, 1, 0],  # vertex 0
    [ 0, 0, 0, 0, 0, 1, 0, 0],  # vertex 1
    [ 0, 0, 0, 0, 1, 0, 0, 0],  # vertex 2
    [ 1, 0, 0, 0, 0, 1, 0, 0],  # vertex 3
    [ 0, 0, 1, 0, 0, 0, 0, 0],  # vertex 4
    [ 0, 1, 0, 1, 0, 0, 0, 0],  # vertex 5
    [ 1, 0, 0, 0, 0, 0, 0, 0],  # vertex 6
    [ 0, 0, 0, 0, 0, 0, 0, 0]   # vertex 7
]

# Call the function and print the result
print(reachability(6, graph))  # Expected output: [3, 0, 6, 5, 1] (order may vary)

def count_components(G: list[list[int]]) -> int:
    """
    Count the number of connected components in a graph.

    Parameters:
    G (list[list[int]]): The adjacency matrix representing the graph.

    Returns:
    int: The number of connected components in the graph.
    """
    def reachability(s: int, G: list[list[int]]) -> list:
        """
        Find all vertices in a graph G reachable from vertex s.

        Parameters:
        s (int): The starting vertex.
        G (list[list[int]]): The adjacency matrix representing the graph.

        Returns:
        list: A list of all vertices reachable from vertex s.
        """
        def dfs(v, visited):
            visited[v] = True
            reachable.append(v)
            for neighbor, is_edge in enumerate(G[v]):
                if is_edge and not visited[neighbor]:
                    dfs(neighbor, visited)

        visited = [False] * len(G)
        reachable = []
        dfs(s, visited)
        return reachable

    # Initialize visited list and component count
    visited = [False] * len(G)
    component_count = 0

    # Iterate through all vertices
    for v in range(len(G)):
        if not visited[v]:
            # Find all vertices in the same component as v
            reachable = reachability(v, G)
            # Mark all reachable vertices as visited
            for vertex in reachable:
                visited[vertex] = True
            # Increment the component count
            component_count += 1

    return component_count


# Test the function with the given adjacency matrix
graph = [
    # 0  1  2  3  4  5  6  7
    [ 0, 0, 0, 1, 0, 0, 1, 0],  # vertex 0
    [ 0, 0, 0, 0, 0, 1, 0, 0],  # vertex 1
    [ 0, 0, 0, 0, 1, 0, 0, 0],  # vertex 2
    [ 1, 0, 0, 0, 0, 1, 0, 0],  # vertex 3
    [ 0, 0, 1, 0, 0, 0, 0, 0],  # vertex 4
    [ 0, 1, 0, 1, 0, 0, 0, 0],  # vertex 5
    [ 1, 0, 0, 0, 0, 0, 0, 0],  # vertex 6
    [ 0, 0, 0, 0, 0, 0, 0, 0]   # vertex 7
]

# Call the function and print the result
print(count_components(graph))  # Expected output: 3