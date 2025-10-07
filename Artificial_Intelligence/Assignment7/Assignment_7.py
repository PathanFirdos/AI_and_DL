# --- Fully Interactive Forward Chaining ---

# Input initial facts
facts_input = input("Enter initial facts separated by commas (e.g., fever,cough): ")
facts = set(f.strip().lower() for f in facts_input.split(","))

# Input rules
rules = []
num_rules = int(input("Enter number of rules: "))

for i in range(num_rules):
    cond_input = input(f"Enter conditions for rule {i+1} separated by commas: ")
    conditions = set(f.strip().lower() for f in cond_input.split(","))
    conclusion = input(f"Enter conclusion for rule {i+1}: ").strip().lower()
    rules.append((conditions, conclusion))

# Forward Chaining Algorithm
def forward_chaining(facts, rules):
    inferred = set()
    added = True

    while added:
        added = False
        for conditions, conclusion in rules:
            if conditions.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                inferred.add(conclusion)
                print(f"Inferred: {conclusion}")
                added = True
    return inferred

# Run Forward Chaining
new_facts = forward_chaining(facts, rules)

print("\nAll facts after inference:", facts)
