# ai_healthbot_full.py

import pandas as pd
import os
import zipfile
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics.pairwise import cosine_similarity

# --- Step 1: Extract dataset from zip if needed ---
zip_path = "Disease prediction based on symptoms.zip"   # Replace with your dataset zip path
extract_folder = "dataset"

if not os.path.exists(extract_folder):
    os.makedirs(extract_folder)

if os.path.exists(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    print(f"Dataset extracted to folder: {extract_folder}")
else:
    print(f"Using existing dataset folder: {extract_folder}")

# --- Step 2: Load CSV ---
csv_file = os.path.join(extract_folder, "dataset.csv")  # Adjust if file name is different
data = pd.read_csv(csv_file)

print("Dataset preview:")
print(data.head())

# --- Step 3: Prepare features ---
X = data['symptoms']        # Symptom descriptions
y = data['disease']         # Disease labels
treatments = data['cures']  # Optional: recommended cures
doctors = data['doctor']    # Optional: recommended doctors

# Convert symptoms text into numerical features
vectorizer = CountVectorizer()
X_vectors = vectorizer.fit_transform(X)

# Train Decision Tree
clf = DecisionTreeClassifier()
clf.fit(X_vectors, y)

# --- Step 4: Prediction function ---
def predict_diseases(symptom_input, top_n=3):
    input_vector = vectorizer.transform([symptom_input])
    similarities = cosine_similarity(input_vector, X_vectors)
    top_indices = similarities[0].argsort()[::-1][:top_n]
    top_diseases = y.iloc[top_indices].tolist()
    top_treatments = treatments.iloc[top_indices].tolist()
    top_doctors = doctors.iloc[top_indices].tolist()
    return list(zip(top_diseases, top_treatments, top_doctors))

# --- Step 5: Chatbot interaction ---
print("\nWelcome to ML HealthBot! Type 'exit' to quit.\n")

while True:
    user_input = input("Enter your symptoms (comma-separated): ").lower()
    if user_input == 'exit':
        print("ML HealthBot: Take care! Goodbye.")
        break
    results = predict_diseases(user_input, top_n=3)
    print("ML HealthBot: Based on your symptoms, possible diseases are:")
    for disease, treatment, doctor in results:
        print(f"- Disease: {disease}\n  Treatment: {treatment}\n  Doctor: {doctor}\n")
