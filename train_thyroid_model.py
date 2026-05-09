import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load thyroid dataset
data = pd.read_csv("dataset/thyroid.csv")

# Show first rows
print(data.head())

# Features and target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Thyroid Model Accuracy:", accuracy)

# Save model
with open("thyroid_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Thyroid model saved successfully!")