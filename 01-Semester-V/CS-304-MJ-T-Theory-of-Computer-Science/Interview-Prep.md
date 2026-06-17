---
title: "CS-304 Theory of Computer Science Interview Preparation"
tags: [cs-304, tcs, theory-of-computation, interview, semester-v]
subject_code: CS-304-MJ-T
type: interview-prep
---

[[00-Dashboard/Home|Home]] | [[01-Semester-V/Semester-V-Dashboard|Semester V]] | [[Overview]] | [[Syllabus]] | [[Unit-1]] | [[Unit-2]] | [[Unit-3]] | [[Unit-4]] | [[Unit-5]] | [[Important-Questions|Imp. Qs]] | [[Revision]] | [[Interview-Prep]]

# Theory of Computer Science Interview Preparation

> [!summary] About
> Top 25+ TCS interview questions categorized by topic, covering Automata, Grammars, and Turing Machines. Often asked in top-tier tech interviews (Google, Amazon, etc.) for compiler and systems roles.

---

## 1. Finite Automata (DFA & NFA)

> [!question] 1. What is the difference between DFA and NFA?
> - **DFA (Deterministic Finite Automaton):** For each state and input symbol, there is exactly *one* transition to a next state. Empty string ($\epsilon$) transitions are not allowed.
> - **NFA (Non-deterministic Finite Automaton):** For a state and input symbol, there can be *zero, one, or multiple* transitions to next states. Empty string ($\epsilon$) transitions are allowed.
> - **Power:** Both DFA and NFA have the *exact same computational power* (they both recognize Regular Languages). Every NFA can be converted to an equivalent DFA using Subset Construction.

> [!question] 2. Explain the terms: Alphabet, String, and Language.
> - **Alphabet ($\Sigma$):** A finite, non-empty set of symbols (e.g., $\Sigma = \{0, 1\}$).
> - **String:** A finite sequence of symbols chosen from some alphabet.
> - **Language:** A set of strings all of which are chosen from some $\Sigma^*$. A language can be finite or infinite.

> [!question] 3. What is the significance of the "Dead State" in a DFA?
> A dead state (or trap state) is a non-accepting state from which there is no escape. Once the automaton enters this state, it stays there for all subsequent inputs. It is used in DFAs to handle invalid inputs since a DFA must have a defined transition for every input symbol from every state.

> [!question] 4. Differentiate between Moore and Mealy Machines.
> Both are Finite State Transducers (produce output):
> - **Moore Machine:** Output depends *only on the current state*. The output length is $|w| + 1$ (where $|w|$ is input length).
> - **Mealy Machine:** Output depends on *both the current state and the current input symbol*. The output length is exactly $|w|$. Mealy machines generally require fewer states than Moore machines.

> [!question] 5. Can we always minimize a DFA? How?
> Yes. Every regular language has a unique minimal DFA. It can be found using the **Table-Filling Method (Myhill-Nerode theorem)**, which involves identifying distinguishable pairs of states (e.g., one accepting, one non-accepting) and merging all pairs of states that cannot be distinguished by any string.

---

## 2. Regular Expressions & Languages

> [!question] 6. What is a Regular Expression (RE)?
> An algebraic description of a regular language. It uses operators like Union ($+$ or $|$), Concatenation ($\cdot$), and Kleene Star ($^*$) to build expressions representing sets of strings.

> [!question] 7. What is the Pumping Lemma for Regular Languages used for?
> It is used *exclusively* to prove that a language is **NOT** regular. It cannot be used to prove a language is regular.
> It states that any sufficiently long string in a regular language can be "pumped" (a middle section repeated any number of times) and the resulting string will still belong to the language.

> [!question] 8. State closure properties of Regular Languages.
> Regular languages are closed under:
> - Union
> - Intersection
> - Concatenation
> - Kleene Star
> - Complement
> - Reversal

---

## 3. Context-Free Grammars (CFG)

> [!question] 9. Define a Context-Free Grammar (CFG).
> A CFG is a 4-tuple $G = (V, T, P, S)$:
> - $V$: Finite set of Variables (Non-terminals)
> - $T$: Finite set of Terminals
> - $P$: Set of Production rules of the form $A \rightarrow \alpha$, where $A \in V$ and $\alpha \in (V \cup T)^*$
> - $S$: Start symbol

> [!question] 10. What is Ambiguity in a grammar?
> A grammar is ambiguous if there exists at least one string in its language that has *more than one distinct leftmost derivation* (or equivalently, more than one distinct Parse Tree).

> [!question] 11. Differentiate between Chomsky Normal Form (CNF) and Greibach Normal Form (GNF).
> - **CNF:** All productions are of the form $A \rightarrow BC$ (two non-terminals) or $A \rightarrow a$ (one terminal). Length of derivation for string of length $n$ is exactly $2n-1$.
> - **GNF:** All productions are of the form $A \rightarrow a\alpha$ (one terminal followed by zero or more non-terminals). Useful for converting CFG to Pushdown Automata.

---

## 4. Push Down Automata (PDA)

> [!question] 12. What is a Push Down Automata (PDA)? How is it different from a DFA?
> A PDA is essentially a Finite Automata equipped with an unbounded **Stack** memory. This allows it to count and match symbols (e.g., matching parentheses, or $a^nb^n$), which a DFA cannot do because a DFA has strictly finite memory (states).

> [!question] 13. What language class does a PDA recognize?
> A PDA recognizes Context-Free Languages (CFLs).

> [!question] 14. What are the two ways a PDA can accept a string?
> 1. **Acceptance by Final State:** The string is fully read, and the PDA ends up in an accepting state.
> 2. **Acceptance by Empty Stack:** The string is fully read, and the stack becomes completely empty. (Both methods are equivalent in power).

---

## 5. Turing Machines (TM) & Computability

> [!question] 15. Describe the structure of a Turing Machine.
> A TM consists of:
> 1. An infinitely long **Tape** divided into cells, initially blank.
> 2. A **Read/Write Head** that can move Left or Right along the tape.
> 3. A **Finite Control** (state machine) that dictates actions.
> It can read, write, change state, and move the head based on the current state and the symbol read.

> [!question] 16. What is the Church-Turing Thesis?
> It hypothesizes that any function that can be computed by a physical step-by-step algorithm can be computed by a Turing Machine. Essentially, the Turing Machine is the mathematical model of a modern computer.

> [!question] 17. What is the Halting Problem?
> The Halting Problem asks: "Given a description of an arbitrary computer program and an input, is it possible to write a program that determines whether the given program will eventually halt (finish) or run forever?"
> **Alan Turing proved this is UNDECIDABLE.** There is no general algorithm that can solve the Halting Problem for all possible programs.

> [!question] 18. What is the Chomsky Hierarchy?
> A containment hierarchy of formal languages:
> 1. **Type 3 (Regular Languages):** Recognized by DFA/NFA.
> 2. **Type 2 (Context-Free Languages):** Recognized by PDA.
> 3. **Type 1 (Context-Sensitive Languages):** Recognized by Linear Bounded Automata (LBA).
> 4. **Type 0 (Recursively Enumerable Languages):** Recognized by Turing Machines.
> `Regular ⊂ Context-Free ⊂ Context-Sensitive ⊂ Recursively Enumerable`

---

[[01-Semester-V/CS-304-MJ-T-Theory-of-Computer-Science/Unit-1|Unit 1]] | [[01-Semester-V/CS-304-MJ-T-Theory-of-Computer-Science/Revision|Revision Summary]]
