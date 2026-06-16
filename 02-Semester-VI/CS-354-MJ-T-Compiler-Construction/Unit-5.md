---
title: "CS-354 Unit 5 - Code Generation and Optimization"
tags: [cs-354, compiler, unit-5]
---

# Unit 5: Code Generation and Optimization

## Intermediate Code Generation
Translates the source program into an intermediate representation (IR) that is machine-independent.
- **Postfix Notation**: Linearized representation of a syntax tree.
- **Three-Address Code (3AC)**: At most three addresses (two operands, one result).
- **Representations of 3AC**:
  - **Quadruples**: (Operator, Arg1, Arg2, Result)
  - **Triples**: Uses pointers to the results instead of temporary variables.
  - **Indirect Triples**: Array of pointers to triples.

## Code Optimization
Improves the intermediate code to make the target code faster and more efficient.
1. **Compile-time Evaluation**: Constant folding.
2. **Common Sub-expression Elimination**: Reusing already computed values.
3. **Dead Code Elimination**: Removing code that does not affect the program outcome.
4. **Frequency Reduction**: Moving loop-invariant code out of loops.
5. **Strength Reduction**: Replacing expensive operations (like multiplication) with cheaper ones (like addition).

## Code Generation
The final phase that maps the optimized IR to the target machine code.
- **Register Allocation**: Assigning variables to registers efficiently.
- **Instruction Selection**: Choosing appropriate target machine instructions.
