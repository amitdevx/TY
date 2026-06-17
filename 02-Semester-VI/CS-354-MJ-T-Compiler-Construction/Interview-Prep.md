---
title: "CS-354 Compiler Construction Interview Preparation"
tags: [cs-354, compiler-design, systems, interview, semester-vi]
subject_code: CS-354-MJ-T
type: interview-prep
---

[[00-Dashboard/Home|Home]] | [[02-Semester-VI/Semester-VI-Dashboard|Semester VI]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]

# Compiler Construction Interview Preparation

> [!summary] About
> Top 20 Compiler Design interview questions. While compiler roles are niche, these concepts are frequently tested in core systems engineering, C++ roles, and performance optimization interviews.

---

## 1. Compiler Phases & Basics

> [!question] 1. What is a Compiler?
> A compiler is a program that translates source code written in a high-level programming language (like C, Java) into a lower-level language (like assembly, machine code, or bytecode) to create an executable program.

> [!question] 2. What are the phases of a Compiler?
> The compilation process is divided into two main parts: Analysis (Front-end) and Synthesis (Back-end).
> 1. Lexical Analysis
> 2. Syntax Analysis (Parsing)
> 3. Semantic Analysis
> 4. Intermediate Code Generation
> 5. Code Optimization
> 6. Target Code Generation
> *(Symbol Table Management and Error Handling run across all phases).*

> [!question] 3. Difference between Compiler and Interpreter?
> - **Compiler:** Scans the entire program and translates it as a whole into machine code. Execution is faster. Errors are displayed after the entire compilation process. Examples: C, C++.
> - **Interpreter:** Translates program one statement at a time. Execution is slower. Errors are displayed for every instruction interpreted. Examples: Python, JavaScript.

> [!question] 4. What is the Symbol Table?
> A data structure maintained by the compiler to keep track of semantics of variables, i.e., it stores information about identifiers (name, type, scope, memory location) encountered in the source program. Hash tables are commonly used for its implementation.

---

## 2. Lexical & Syntax Analysis

> [!question] 5. What is Lexical Analysis?
> The first phase of a compiler. It reads the source code character by character, groups them into lexemes, and produces a sequence of **Tokens**. It also removes whitespace and comments. Tool used: **Lex/Flex**.

> [!question] 6. What is Syntax Analysis (Parsing)?
> The second phase. It takes the tokens produced by lexical analysis as input and generates a **Parse Tree** (or Syntax Tree). It checks if the given input string can be derived from the grammar of the programming language. Tool used: **Yacc/Bison**.

> [!question] 7. What is a Token, Lexeme, and Pattern?
> - **Token:** An abstract symbol representing a lexical unit (e.g., `IDENTIFIER`, `NUMBER`, `KEYWORD`).
> - **Lexeme:** The actual sequence of characters in the source code that matches the pattern for a token (e.g., `count`, `42`, `while`).
> - **Pattern:** The rule (usually a Regular Expression) that describes the set of lexemes that can form a particular token.

> [!question] 8. Differentiate between Top-Down and Bottom-Up Parsing.
> - **Top-Down Parsing:** Constructs the parse tree from the root (start symbol) down to the leaves. Examples: Recursive Descent, LL(1). Uses Leftmost Derivation.
> - **Bottom-Up Parsing:** Constructs the parse tree from the leaves up to the root. Examples: Shift-Reduce, LR(0), SLR, LALR. Uses Rightmost Derivation in reverse.

> [!question] 9. What is Left Recursion and why is it a problem?
> A grammar is left-recursive if it has a non-terminal $A$ such that there is a derivation $A \rightarrow A\alpha$. It is a problem for Top-Down parsers because they can enter an infinite loop trying to expand $A$. It must be eliminated before parsing.

---

## 3. Semantic Analysis & Intermediate Code

> [!question] 10. What does Semantic Analysis do?
> It checks the source program for semantic errors and gathers type information. Key tasks include **Type Checking** (e.g., ensuring you don't add a string to an integer), Scope Resolution, and checking for undeclared variables.

> [!question] 11. What is an Abstract Syntax Tree (AST)?
> An AST is a condensed version of a parse tree where operators are interior nodes and the operands are the children of that node. It removes unnecessary syntactic details like parentheses and semicolons.

> [!question] 12. What is Intermediate Code? Why generate it?
> Intermediate Code is a machine-independent representation of the source code.
> **Why:** It separates the front-end (language-specific) from the back-end (machine-specific). This allows the creation of multi-language, multi-target compilers (like LLVM or GCC) and enables machine-independent optimizations.

> [!question] 13. What is Three-Address Code (TAC)?
> A form of intermediate code where each instruction has at most three operands (two for operands, one for the result) and one operator.
> Example: `x = y + z`
> Complex expressions are broken down using temporary variables: `a = b + c * d` becomes `t1 = c * d; a = b + t1`.

---

## 4. Code Optimization & Generation

> [!question] 14. What are the criteria for Code Optimization?
> - The optimized code must preserve the exact semantic meaning of the original program.
> - The optimized code must run faster or use less memory (or both).
> - The compilation time overhead for optimization should be reasonable.

> [!question] 15. Explain Loop Optimization techniques.
> Loops are the most crucial part for optimization because programs spend most of their time inside loops.
> - **Code Motion:** Moving computations outside the loop if they produce the same result every iteration (loop-invariant code).
> - **Strength Reduction:** Replacing expensive operations with cheaper ones (e.g., replacing $x \times 2$ with $x + x$ or bit shift).
> - **Loop Unrolling:** Replicating the loop body to decrease the number of condition checks and branches.

> [!question] 16. What is a Basic Block and a Flow Graph?
> - **Basic Block:** A sequence of consecutive statements in which flow of control enters at the beginning and leaves at the end without halt or possibility of branching except at the end.
> - **Flow Graph:** A directed graph where nodes are basic blocks and edges indicate which block can follow which other block. Used for control flow analysis.

> [!question] 17. Explain Peep-hole Optimization.
> A very simple, local optimization technique applied to the final target code. It examines a short sequence of target instructions (the "peep-hole") and replaces them with a shorter or faster sequence whenever possible.
> Example: Eliminating redundant loads/stores (e.g., storing a register to memory and immediately loading it back).

---

[[02-Semester-VI/CS-354-MJ-T-Compiler-Construction/Revision|Revision Summary]] | [[02-Semester-VI/CS-354-MJ-T-Compiler-Construction/Unit-1|Unit 1]]
