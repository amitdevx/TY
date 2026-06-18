# Assignment 2: Informed Search Techniques

## Problem Statement / Aim
To implement and understand informed search techniques, specifically the A* (A-Star) search algorithm, to find the optimal path between two nodes in a graph using a heuristic function.

## Theory & Concept
A* Search is an informed search algorithm that aims to find the lowest-cost path from a given initial node to a goal node. It uses a best-first search approach and finds the least-cost path by maintaining a priority queue of nodes to be explored. A* uses an evaluation function `f(n) = g(n) + h(n)`, where:
- `g(n)` is the actual cost from the start node to node `n`.
- `h(n)` is the estimated cost (heuristic) from node `n` to the goal node.
If the heuristic is admissible (never overestimates the true cost), A* is guaranteed to find the optimal path.

## Fully Solved Code
```python
import heapq

def a_star_search(graph, start, goal, heuristics):
    # Priority queue stores (f_cost, current_node, path, g_cost)
    open_list = [(heuristics[start], start, [start], 0)]
    closed_set = set()

    while open_list:
        f_cost, current_node, path, g_cost = heapq.heappop(open_list)

        if current_node == goal:
            return path, g_cost

        if current_node in closed_set:
            continue

        closed_set.add(current_node)

        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in closed_set:
                new_g_cost = g_cost + weight
                new_f_cost = new_g_cost + heuristics[neighbor]
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(open_list, (new_f_cost, neighbor, new_path, new_g_cost))

    return None, float('inf')

if __name__ == "__main__":
    # Graph representing cities and distances (weights)
    graph = {
        'S': [('A', 1), ('B', 4)],
        'A': [('B', 2), ('C', 5), ('G', 12)],
        'B': [('C', 2)],
        'C': [('G', 3)],
        'G': []
    }
    
    # Heuristic (estimated distance to goal 'G')
    heuristics = {
        'S': 7,
        'A': 6,
        'B': 2,
        'C': 1,
        'G': 0
    }
    
    start_node = 'S'
    goal_node = 'G'
    
    print("A* Search Algorithm Execution:")
    path, cost = a_star_search(graph, start_node, goal_node, heuristics)
    
    if path:
        print(f"Optimal Path found: {' -> '.join(path)}")
        print(f"Total Cost: {cost}")
    else:
        print("No path found.")
```

## Expected Output
```text
A* Search Algorithm Execution:
Optimal Path found: S -> A -> B -> C -> G
Total Cost: 8
```

[[CS-321-Viva-2|View Viva Questions]]
