import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("labeled_complaints_500.csv")
print(df)

# Preprocess text
from preprocess import preprocess_text
df["clean_text"] = df["email_text"].apply(preprocess_text)

# Train model
X_train, X_test, y_train, y_test = train_test_split(df["clean_text"], df["category"], test_size=0.2, random_state=42)
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Save model and vectorizer
pickle.dump(model, open("email_classifier.pkl", "wb"))
pickle.dump(vectorizer, open("tfidf_vectorizer.pkl", "wb"))

print("Model trained and saved successfully!")
