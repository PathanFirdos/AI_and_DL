# --- Interactive Backward Chaining ---

# Step 1: Input initial facts
facts_input = input("Enter initial facts separated by commas (e.g., fever,cough): ")
facts = set(f.strip().lower() for f in facts_input.split(","))

# Step 2: Input rules
rules = {}
num_rules = int(input("Enter number of rules: "))
for i in range(num_rules):
    conclusion = input(f"Enter conclusion for rule {i+1}: ").strip().lower()
    cond_input = input(f"Enter conditions for rule {i+1} separated by commas: ")
    conditions = set(f.strip().lower() for f in cond_input.split(","))
    rules[conclusion] = conditions

# Step 3: Input goal/query
goal = input("Enter the goal/fact you want to infer: ").strip().lower()

# Step 4: Backward Chaining function
def backward_chaining(goal, facts, rules):
    if goal in facts:
        print(f"{goal} is already a known fact.")
        return True

    if goal in rules:
        conditions = rules[goal]
        print(f"Checking conditions for '{goal}': {conditions}")
        for cond in conditions:
            if not backward_chaining(cond, facts, rules):
                print(f"Condition '{cond}' for '{goal}' not satisfied.")
                return False
        print(f"All conditions for '{goal}' satisfied. '{goal}' inferred.")
        facts.add(goal)
        return True

    print(f"No rule to infer '{goal}'.")
    return False

# Step 5: Run Backward Chaining
result = backward_chaining(goal, facts, rules)

print("\nResult:", f"{goal} can be inferred" if result else f"{goal} cannot be inferred")
print("Facts after inference:", facts)
