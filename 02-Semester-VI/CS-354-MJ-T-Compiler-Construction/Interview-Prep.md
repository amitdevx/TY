---
title: "CS-354 Compiler Construction Interview Prep"
tags: [cs-354, compiler, interview]
---

# Compiler Construction Interview Preparation

1. **What are the phases of a compiler?**
   Lexical analysis, syntax analysis, semantic analysis, intermediate code generation, optimization, and code generation.
2. **Difference between compiler and interpreter?**
   Compiler translates the entire source code at once. Interpreter translates and executes line by line.
3. **What is Left Recursion and why is it a problem?**
   It causes top-down parsers to enter infinite loops.
4. **Explain FIRST and FOLLOW sets.**
   FIRST set contains terminals that begin derived strings. FOLLOW set contains terminals that can appear after a non-terminal.
5. **What is the difference between LL and LR parsing?**
   LL is Top-Down, processes Left-to-right, produces Leftmost derivation. LR is Bottom-Up, produces Rightmost derivation in reverse.
6. **What is an ambiguous grammar?**
   A grammar that produces more than one parse tree for a single input string.
