import streamlit as st
from langchain_community.llms import OpenAI

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="GeekCook - Recipe AI",
    page_icon="🍳",
    layout="centered"
)

# -------------------------------
# TITLE
# -------------------------------
st.title("🍳 GeekCook || Recipe Recommendation System")
st.markdown("Get delicious recipes based on ingredients you have!")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.header("🔑 API Configuration")

import os
openai_api_key = os.getenv("OPENAI_API_KEY")
st.write("API KEY:", openai_api_key)
# if not openai_api_key:
#     st.error("API key not found. Please configure secrets.")
#     st.stop()

# -------------------------------
# FUNCTION: GENERATE RECIPES
# -------------------------------

def generate_recommendations(input_text):
    try:
        openai.api_key = openai_api_key

        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Given the ingredients: {input_text}, suggest a step-by-step recipe.",
            max_tokens=300,
            temperature=0.7
        )

        return response.choices[0].text.strip()

    except Exception as e:
        return f"Error: {str(e)}"

# -------------------------------
# USER INPUT FORM
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
        st.warning("⚠️ Please enter your OpenAI API key.")
    
    elif not user_input.strip():
        st.warning("⚠️ Please enter some ingredients.")
    
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