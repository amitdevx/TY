[[CS-321-Assignment-4|Back to Assignment]]

# Viva Questions: Game Playing Algorithms

1. **What is the Minimax algorithm?**
   *Minimax is an adversarial search algorithm used to determine the optimal move for a player in zero-sum games, assuming the opponent plays perfectly to minimize your score.*

2. **Why do we subtract or add `depth` in the evaluation score inside Minimax?**
   *Adding/subtracting the depth penalizes longer games, forcing the AI to choose a win in the fewest possible moves or delay a loss as much as possible.*

3. **What are zero-sum games?**
   *Zero-sum games are situations where one player's gain is exactly equal to the other player's loss. For example, if player A wins (+1), player B loses (-1).*

4. **What is Alpha-Beta Pruning?**
   *It is an optimization technique for the Minimax algorithm that reduces the number of nodes evaluated by the search tree by "pruning" branches that cannot possibly influence the final decision.*

5. **Does Alpha-Beta pruning change the final decision of the Minimax algorithm?**
   *No, Alpha-Beta pruning always finds the exact same move as standard Minimax, it simply does so much faster by skipping redundant evaluations.*
