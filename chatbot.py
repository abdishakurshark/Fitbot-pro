
import streamlit as st

# Add a title
st.title("FITBOT")

# Input from the user (weight, height)
weight = st.number_input("Enter your weight (kg):")
height = st.number_input("Enter your height (cm):")

if weight and height:
    # Example of using your chatbot logic here
    # (Replace this with your chatbot response logic)
    bmi = weight / ((height / 100) ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.write("Recommendation: Gain weight")
    elif 18.5 <= bmi < 24.9:
        st.write("Recommendation: Maintain weight")
    else:
        st.write("Recommendation: Lose weight")
    
