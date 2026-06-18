# Assignment 5: Knowledge Representation and Logical Reasoning

## Problem Statement / Aim
To study knowledge representation techniques and implement a simple logical reasoning engine using the Forward Chaining algorithm.

## Theory & Concept
Knowledge representation enables AI systems to understand and reason about the world. A common way to represent logic is using a rule-based system composed of facts and IF-THEN rules. 
Logical reasoning applies inference rules to this knowledge base. Forward Chaining is a data-driven reasoning method that starts with a set of known facts, applies inference rules to extract new facts, and iterates this process until a desired goal is reached or no more facts can be inferred. It is widely used in expert systems.

## Fully Solved Code
```python
def forward_chaining(kb_rules, known_facts, query):
    inferred = set(known_facts)
    new_facts_added = True
    
    print(f"Initial Facts: {inferred}")
    
    while new_facts_added:
        new_facts_added = False
        
        for rule in kb_rules:
            premises, conclusion = rule
            
            # If all premises of the rule are known and conclusion is not yet inferred
            if all(p in inferred for p in premises) and conclusion not in inferred:
                print(f"Applying rule: IF {premises} THEN {conclusion}")
                inferred.add(conclusion)
                new_facts_added = True
                
                # Check if we have derived the target query
                if conclusion == query:
                    print(f"Query '{query}' inferred successfully!")
                    return True
                    
    print(f"Query '{query}' could not be inferred.")
    return False

if __name__ == "__main__":
    # Knowledge Base: represented as a list of rules (premises, conclusion)
    # e.g., (["Croaks", "Eats Flies"], "Frog") => IF Croaks AND Eats Flies THEN Frog
    rules = [
        (["Has Hair"], "Mammal"),
        (["Gives Milk"], "Mammal"),
        (["Has Feathers"], "Bird"),
        (["Flies", "Lays Eggs"], "Bird"),
        (["Mammal", "Eats Meat"], "Carnivore"),
        (["Mammal", "Has Pointy Teeth", "Has Claws"], "Carnivore"),
        (["Carnivore", "Has Tawny Color", "Has Dark Spots"], "Cheetah"),
        (["Carnivore", "Has Tawny Color", "Has Black Stripes"], "Tiger")
    ]
    
    # Starting Facts
    facts = ["Has Hair", "Has Pointy Teeth", "Has Claws", "Has Tawny Color", "Has Black Stripes"]
    
    target_query = "Tiger"
    
    print("Starting Forward Chaining Inference Engine...\n")
    result = forward_chaining(rules, facts, target_query)
    
    print(f"\nFinal Known Facts: {facts}")
    print(f"Was '{target_query}' proven? {result}")
```

## Expected Output
```text
Starting Forward Chaining Inference Engine...

Initial Facts: {'Has Tawny Color', 'Has Black Stripes', 'Has Hair', 'Has Pointy Teeth', 'Has Claws'}
Applying rule: IF ['Has Hair'] THEN Mammal
Applying rule: IF ['Mammal', 'Has Pointy Teeth', 'Has Claws'] THEN Carnivore
Applying rule: IF ['Carnivore', 'Has Tawny Color', 'Has Black Stripes'] THEN Tiger
Query 'Tiger' inferred successfully!

Final Known Facts: ['Has Hair', 'Has Pointy Teeth', 'Has Claws', 'Has Tawny Color', 'Has Black Stripes']
Was 'Tiger' proven? True
```

[[CS-321-Viva-5|View Viva Questions]]
