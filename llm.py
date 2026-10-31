import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("GROQ_API_KEY")
if not api_key:
        raise HTTPException(status_code=500, detail="Missing GROQ_API_KEY in environment")

client = Groq()

def generate_workout_plan(model,   fitness_goal, experience_level, days_per_week, equipment_access, injuries):
    prompt = f"""
    Create a personalized workout plan.
    User Profile:
    - Goal: {fitness_goal}
    - Experience: {experience_level}
    - Days Available: {days_per_week}
    - Equipment: {equipment_access}
    - Injuries/Limitations: {injuries if injuries else 'None'}
    Requirements:
    1. Start immediately with the weekly workout schedule.
    2. Allocate at least 80% of the response to the workout plan.
    3. Do NOT provide lengthy introductions.
    4. Do NOT provide general fitness advice.
    5. Do NOT provide nutrition advice.
    6. Do NOT use markdown tables.
    7. Use bullet points only.
    8. For each day include:
    - Exercises
    - Sets
    - Reps
    - Rest time
    9. Limit recovery notes to 2 lines maximum.
    """
    response = client.chat.completions.create(
        model= model,
        messages=[
                {
                "role": "system",
                "content": "You are an expert fitness coach."
                },
                {
                "role": "user",
                "content": prompt
                }
                ],
                temperature=0.7,
                max_tokens = 700,
            )
    return response.choices[0].message.content

        


    
