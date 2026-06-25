[[CS-321-Assignment-2|Back to Assignment]]

# Viva Questions: Informed Search Techniques

1. **What is the A\* search algorithm?**
   *A\* is an informed search algorithm that uses an evaluation function `f(n) = g(n) + h(n)` to find the shortest path from a start node to a goal node efficiently.*

2. **What does `g(n)` and `h(n)` represent in A\* search?**
   *`g(n)` is the exact cost from the start node to the current node `n`. `h(n)` is the heuristic estimated cost from node `n` to the goal node.*

3. **What is an admissible heuristic?**
   *A heuristic is admissible if it never overestimates the actual cost to reach the goal. Admissibility guarantees that A\* will find the optimal path.*

4. **Can A\* search be used for unweighted graphs?**
   *Yes, if edge costs are uniform, A\* acts like BFS but guided by a heuristic. If `h(n) = 0` for all nodes, A\* behaves exactly like Dijkstra's algorithm.*

5. **What is the main drawback of the A\* algorithm?**
   *A\* stores all generated nodes in memory (in the open and closed lists), which makes its space complexity O(b^d), where b is the branching factor and d is the depth. This can lead to memory exhaustion for large problems.*
