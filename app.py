import streamlit as st
import os
from openai import OpenAI

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Recipe Recommendation System",
    page_icon="🍳",
    layout="centered"
)

# -------------------------------
# TITLE
# -------------------------------
st.title("🍳 Recipe Recommendation System")
st.markdown("Get delicious recipes based on ingredients you have!")

# -------------------------------
# API KEY
# -------------------------------
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

# -------------------------------
# FUNCTION
# -------------------------------
def generate_recommendations(input_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Given the ingredients: {input_text}

                    Generate:
                    - Recipe Name
                    - Ingredients
                    - Step-by-step Instructions
                    - Cooking Time
                    """
                }
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"

# -------------------------------
# FORM
# -------------------------------
with st.form("recipe_form"):
    user_input = st.text_area(
        "🥕 Enter ingredients (comma separated):",
        placeholder="e.g., tomato, onion, cheese, pasta"
    )

    submitted = st.form_submit_button("🍽️ Get Recipe")

# -------------------------------
# OUTPUT
# -------------------------------
if submitted:
    if not openai_api_key:
        st.error("API key not configured.")
    
    elif not user_input.strip():
        st.warning("Please enter some ingredients.")
    
    else:
        with st.spinner("👨‍🍳 Cooking up your recipe..."):
            result = generate_recommendations(user_input)

        st.success("✅ Here's your recipe!")
        st.markdown(result)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit + AI")