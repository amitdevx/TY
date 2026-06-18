[[CS-321-Assignment-1|Back to Assignment]]

# Viva Questions: Problem Solving Using Search

1. **What is the difference between uninformed and informed search?**
   *Uninformed search algorithms (like BFS, DFS) have no additional information about the goal state other than the problem definition, while informed search algorithms (like A*) use heuristics to guide the search.*

2. **Why does BFS guarantee the shortest path in an unweighted graph?**
   *BFS explores nodes level by level, ensuring that it visits all nodes at distance `k` before visiting any node at distance `k+1`. Thus, the first time it reaches the goal, it must be via the shortest path.*

3. **What data structure is typically used to implement Breadth-First Search?**
   *A Queue (FIFO) is used to implement BFS to ensure nodes are processed in the order they were discovered.*

4. **What is the time and space complexity of BFS?**
   *Time complexity is O(V + E) and space complexity is O(V), where V is the number of vertices and E is the number of edges.*

5. **When would you prefer Depth-First Search (DFS) over Breadth-First Search (BFS)?**
   *DFS is preferred when the memory is limited (as it requires less space than BFS) or when the target node is known to be deep in the tree. BFS is preferred if the solution is close to the root.*
