# Assignment 1: Problem Solving Using Search

## Problem Statement / Aim
To implement and understand problem solving using uninformed search algorithms, specifically Breadth-First Search (BFS), to traverse a graph and find a path from a start state to a goal state.

## Theory & Concept
Breadth-First Search (BFS) is an uninformed search algorithm that starts at the root node and explores all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. It uses a queue data structure to keep track of the nodes to be explored. BFS is optimal for finding the shortest path in an unweighted graph because it always explores nodes in order of their distance from the source.

## Fully Solved Code
```python
from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
            visited.add(node)
    return None

if __name__ == "__main__":
    # Representing a graph using an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B', 'H'],
        'F': ['C'],
        'G': ['C'],
        'H': ['E']
    }
    
    start_node = 'A'
    goal_node = 'H'
    
    print(f"Graph representation: {graph}")
    print(f"Finding path from {start_node} to {goal_node} using BFS...")
    
    path = bfs(graph, start_node, goal_node)
    
    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found.")
```

## Expected Output
```text
Graph representation: {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F', 'G'], 'D': ['B'], 'E': ['B', 'H'], 'F': ['C'], 'G': ['C'], 'H': ['E']}
Finding path from A to H using BFS...
Path found: A -> B -> E -> H
```

[[CS-321-Viva-1|View Viva Questions]]
