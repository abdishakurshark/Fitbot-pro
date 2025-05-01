import streamlit as st

# Add a title
st.title("FITBOT 💪")

# User information
weight = st.number_input("Enter your weight (kg):", min_value=30.0, max_value=200.0, value=70.0)
height = st.number_input("Enter your height (cm):", min_value=100.0, max_value=250.0, value=170.0)
goal = st.selectbox("What's your primary goal?", ["Weight loss", "Muscle gain", "Maintenance"])
fitness_level = st.selectbox("Your fitness level:", ["Beginner", "Intermediate", "Advanced"])

# BMI Calculation
if st.button("Get Fitness Plan"):
    bmi = weight / ((height / 100) ** 2)
    st.subheader(f"Your BMI: {bmi:.2f}")
    
    # BMI Analysis
    if bmi < 18.5:
        st.write("You're underweight. Let's build some muscle!")
    elif 18.5 <= bmi < 24.9:
        st.write("You're at a healthy weight. Let's maintain or improve!")
    else:
        st.write("You're overweight. Let's focus on healthy weight loss.")
    
    st.markdown("---")
    
    # Workout Recommendations
    st.subheader("🏋️ Workout Plan")
    if goal == "Weight loss":
        st.write("""
        - 30-45 mins cardio (running, cycling, swimming) 5x/week
        - Full body strength training 3x/week
        - HIIT workouts 2x/week
        """)
    elif goal == "Muscle gain":
        st.write("""
        - Strength training 4-5x/week (focus on progressive overload)
        - Split routine (e.g., push/pull/legs)
        - 8-12 reps per set, 3-4 sets per exercise
        """)
    else:  # Maintenance
        st.write("""
        - Balanced routine: 3x strength, 2x cardio, 1x flexibility
        - Try new activities to prevent boredom
        """)
    
    # Dietary Plan
    st.subheader("🍎 Nutrition Plan")
    if goal == "Weight loss":
        st.write("""
        - 500 calorie deficit daily
        - High protein (1.6-2.2g per kg body weight)
        - Focus on whole foods, vegetables, lean proteins
        - Example meal: Grilled chicken with quinoa and broccoli
        """)
    elif goal == "Muscle gain":
        st.write("""
        - 300-500 calorie surplus daily
        - High protein (2.2-2.5g per kg body weight)
        - Carbs around workouts
        - Example meal: Salmon with sweet potato and asparagus
        """)
    else:  # Maintenance
        st.write("""
        - Maintain current calorie intake
        - Balanced macros (40% carbs, 30% protein, 30% fat)
        - Variety of colorful vegetables
        """)
    
    # Gym Tips Section
    st.subheader("🏢 Gym Pro Tips")
    st.write("""
    - Always warm up for 5-10 minutes
    - Focus on form over weight
    - Wipe down equipment after use
    - Rest 30-90 seconds between sets
    - Stay hydrated (bring a water bottle)
    """)
    
    # Exercise Examples
    st.subheader("💪 Exercise Examples")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Upper Body:**")
        st.write("- Push-ups")
        st.write("- Pull-ups")
        st.write("- Dumbbell presses")
    with col2:
        st.write("**Lower Body:**")
        st.write("- Squats")
        st.write("- Lunges")
        st.write("- Deadlifts")

# Chatbot feature
st.markdown("---")
st.subheader("Ask FitBot Anything")
user_question = st.text_input("Type your fitness question here:")

if user_question:
    user_question = user_question.lower()
    
    # Workout questions
    if any(word in user_question for word in ["workout", "exercise", "train", "routine"]):
        st.write("FitBot: For workout plans, focus on compound movements like squats, deadlifts, and bench presses. Aim for 3-5 sets of 8-12 reps for muscle growth.")
    
    # Diet questions
    elif any(word in user_question for word in ["diet", "food", "eat", "nutrition"]):
        st.write("FitBot: A balanced diet should include protein (chicken, fish, tofu), complex carbs (rice, quinoa), healthy fats (avocados, nuts), and plenty of vegetables.")
    
    # Gym questions
    elif any(word in user_question for word in ["gym", "equipment", "etiquette", "machine"]):
        st.write("FitBot: Remember to re-rack weights, wipe down machines after use, and be mindful of others' space. Ask staff if you're unsure how to use equipment.")
    
    # General advice
    else:
        st.write("FitBot: For best results, combine consistent training with proper nutrition and adequate rest. Most people need 7-9 hours of sleep for optimal recovery.")
