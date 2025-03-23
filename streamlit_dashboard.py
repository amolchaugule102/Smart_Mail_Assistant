import streamlit as st
import pandas as pd
from classify_emails import classify_email

# Set page config
st.set_page_config(page_title="Smart Email Classifier", page_icon="📩", layout="centered")

# Apply background styling
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a banner image
st.image("email_banner.jpg", use_column_width=True)  # Make sure this image exists in your folder

# App Title
st.title("📧 Smart Email Assistant for Power Grid Companies⚡")

# Input field with placeholder text
email_text = st.text_area("✍️ Enter an email below:", placeholder="Type or paste an email here...")

# Classification Button
if st.button("🚀 Classify Email"):
    if email_text:
        category = classify_email(email_text)
        
        # Show a success message with animation
        st.success(f"✅ Predicted Category: **{category}**")
        
        # Display different emojis based on category
        category_emojis = {
            "Power Outage": "⚡",
            "Billing Issue": "💰",
            "Technical Complaint": "🔧",
            "General Inquiry": "ℹ️"
        }
        st.markdown(f"**Category Details:** {category_emojis.get(category, '📩')} {category}")

    else:
        st.warning("⚠️ Please enter an email before classifying.")

# Footer
st.markdown("---")
st.markdown("💡 *Developed with ❤️ using NLP and Machine Learning*")


