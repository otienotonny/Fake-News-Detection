app_code = '''
import streamlit as st
import joblib

# Load the saved model
model = joblib.load("fake_news_model.pkl")

# App title and description
st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("📰 Fake News Detection App")
st.write("Enter a news article or headline, and we'll tell you if it's likely fake or real.")

# Input area
text_input = st.text_area("Paste news content here:", height=200)

if st.button("Predict"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        try:
            prediction = model.predict([text_input])[0]
            if prediction == 1:
                st.success("✅ This appears to be Real News.")
            else:
                st.error("❌ This appears to be Fake News.")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
'''
with open("app.py", "w") as f:
    f.write(app_code)
print("✅ app.py file created successfully.")
