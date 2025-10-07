# --- Dynamic Medical Chatbot ---

def dynamic_medical_chatbot():
    print("Welcome to Dynamic HealthBot! Type 'exit' to quit.\n")
    
    # Empty rules dictionary
    rules = {}

    # Step 1: Add rules interactively
    num_rules = int(input("Enter number of rules you want to add: "))
    for i in range(num_rules):
        symptoms_input = input(f"Enter symptoms for rule {i+1} (separated by spaces): ").lower().strip()
        disease = input(f"Enter the disease or advice for these symptoms: ").strip()
        rules[symptoms_input] = disease
    
    print("\nRules added successfully! Start chatting with HealthBot.")
    
    # Step 2: Chat loop
    while True:
        user_input = input("\nYou: ").lower().strip()
        if user_input == "exit":
            print("HealthBot: Take care! Goodbye.")
            break

        found = False
        for symptoms, response in rules.items():
            # Check if all symptoms in rule are in user input
            if all(symptom in user_input for symptom in symptoms.split()):
                print(f"HealthBot: {response}")
                found = True
                break
        
        if not found:
            print("HealthBot: Sorry, I cannot determine your condition. Please consult a doctor.")

# Run the chatbot
dynamic_medical_chatbot()

