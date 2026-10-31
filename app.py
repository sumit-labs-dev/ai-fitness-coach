import streamlit as st
from llm import generate_workout_plan
import os

model = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

st.title("AI Fitness Coach")

fitness_goal = st.selectbox(
    "Fitness Goal",
    [
        "Build muscle", "Lose fat", "General fitness", "Improve endurance"
    ], index = 1
)

experience_level = st.selectbox(
    "Experience Level",
    [
        "Beginner", "Intermediate", "Advanced"
    ], index = 0
)

days_per_week = st.slider(
    "Days Available Per Week",
    min_value=1, max_value=7, value=3
)

injuries = st.text_area(
    "Injuries or Limitations (Optional)",
    placeholder="e.g. bad knees, lower back pain, no overhead pressing"
)

equipment_access = st.selectbox(
    "Equipment Access",
    [
        "No equipment", "Home dumbbells", "Full gym"
    ], index = 0
)

st.write("### Selected Options")
st.write(f"**Fitness Goal:** {fitness_goal}")
st.write(f"**Experience Level:** {experience_level}")
st.write(f"**Days Available Per Week:** {days_per_week}")
st.write(f"**Injuries or Limitations:** {injuries}")
st.write(f"**Equipment Access:** {equipment_access}")

# prompt = ''

if st.button("Generate Workout Plan"):
    try:
        with st.spinner("Generating your workout plan..."):
            plan = generate_workout_plan(
                model=model,
                fitness_goal=fitness_goal,
                experience_level=experience_level,
                days_per_week=days_per_week,
                equipment_access=equipment_access,
                injuries=injuries,
            )
            st.write("Response received ✅")
            # st.write(response)
            if plan:
                st.markdown("## Your Personalized Workout Plan")
                st.markdown(plan)
            else:
                st.warning("The model returned an empty response. Please try again in some time")
    except Exception as e:
            st.error(f"Error is {e}")


        


    
