import pickle
from preprocess import preprocess_text

# Load model & vectorizer
model = pickle.load(open("email_classifier.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

def classify_email(email_text):
    clean_text = preprocess_text(email_text)
    transformed_text = vectorizer.transform([clean_text])
    return model.predict(transformed_text)[0]

# Test classification
email = "My electricity bill is too high this month!"
print(f"Predicted Category: {classify_email(email)}")
