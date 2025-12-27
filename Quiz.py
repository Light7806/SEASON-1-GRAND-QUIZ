import streamlit as st
import time

def main():
    # Page Configuration
    st.set_page_config(
        page_title="Season 1: The Opening - Final Exam",
        page_icon="🐍",
        layout="centered"
    )

    # --- HEADER SECTION ---
    st.title("🐍 Season 1: The Opening")
    st.caption("Final Exam")
    st.markdown("""
    **Instructions:**
    * There are **18 Questions** covering the entire season.
    * Topics: Basics, NumPy, Pandas, Matplotlib, OOPs, and File Handling.
    * You need **65%** to pass the exam.
    """)
    st.markdown("---")

    # --- QUESTION BANK (18 Questions) ---
    quiz_data = [
        # --- EPISODE 1: THE BASICS (3 Questions) ---
        {
            "question": "1. Which keyword is used to define a function in Python?",
            "options": ["func", "def", "function", "define"],
            "answer": "def"
        },
        {
            "question": "2. Which brackets are used to create a List?",
            "options": ["( )", "{ }", "[ ]", "< >"],
            "answer": "[ ]"
        },
        {
            "question": "3. What is the output of `print(10 % 3)`?",
            "options": ["3", "3.33", "1", "10"],
            "answer": "1"
        },

        # --- EPISODE 2: DATA STRUCTURES & NUMPY (4 Questions) ---
        {
            "question": "4. If you create a Set `s = {1, 2, 2, 3}`, what will it store?",
            "options": ["{1, 2, 2, 3}", "{1, 2, 3}", "[1, 2, 2, 3]", "Error"],
            "answer": "{1, 2, 3}"
        },
        {
            "question": "5. In a Dictionary, how do you access a value?",
            "options": ["Using its Index (0, 1...)", "Using its Key", "Using .get_value()", "Using round brackets ()"],
            "answer": "Using its Key"
        },
        {
            "question": "6. NumPy Broadcasting allows you to:",
            "options": ["Download data faster", "Perform math on an entire array at once", "Create 3D games", "Hide data"],
            "answer": "Perform math on an entire array at once"
        },
        {
            "question": "7. Which NumPy function changes the shape of an array (e.g., from 1D to 2D)?",
            "options": ["resize", "reshape", "change_dim", "transform"],
            "answer": "reshape"
        },

        # --- EPISODE 3: PANDAS & MATPLOTLIB (4 Questions) ---
        {
            "question": "8. In Pandas, which command is used to select a specific ROW by index?",
            "options": ["df.row()", "df.select()", "df.iloc[]", "df['row']"],
            "answer": "df.iloc[]"
        },
        {
            "question": "9. How do you completely delete rows that have missing (NaN) values?",
            "options": ["df.fillna()", "df.delete()", "df.dropna()", "df.remove()"],
            "answer": "df.dropna()"
        },
        {
            "question": "10. You wrote `plt.plot()`, but the graph isn't appearing. What are you missing?",
            "options": ["plt.show()", "plt.render()", "plt.print()", "plt.open()"],
            "answer": "plt.show()"
        },
        {
            "question": "11. Which plot is best for comparing categories (e.g., GPT vs Gemini)?",
            "options": ["Scatter Plot", "Line Chart", "Bar Chart", "Pie Chart"],
            "answer": "Bar Chart"
        },

        # --- EPISODE 4: OOPs (4 Questions) ---
        {
            "question": "12. How do you make a variable PRIVATE in a Python Class (Encapsulation)?",
            "options": ["By writing 'private'", "By using double underscore (__)", "By using a hashtag #", "By using Capital letters"],
            "answer": "By using double underscore (__)"
        },
        {
            "question": "13. Two classes have a function with the SAME name but DIFFERENT behaviors. This is called:",
            "options": ["Inheritance", "Polymorphism", "Looping", "Debugging"],
            "answer": "Polymorphism"
        },
        {
            "question": "14. Which function is automatically called when you create a new Object?",
            "options": ["__init__", "__start__", "__main__", "__setup__"],
            "answer": "__init__"
        },
        {
            "question": "15. What does the `self` keyword represent in a class?",
            "options": ["The Python Language", "The Current Object Instance", "The Parent Class", "Global Variables"],
            "answer": "The Current Object Instance"
        },

        # --- EPISODE 5: FILES & EXCEPTIONS (3 Questions) ---
        {
            "question": "16. In Exception Handling, when does the `finally` block run?",
            "options": ["Only if there is an Error", "Only if there is NO Error", "Always (No matter what)", "Never"],
            "answer": "Always (No matter what)"
        },
        {
            "question": "17. To save an AI Model using Pickle, which mode must be used?",
            "options": ["'w' (Write Text)", "'wb' (Write Binary)", "'r' (Read)", "'a' (Append)"],
            "answer": "'wb' (Write Binary)"
        },
        {
            "question": "18. Why is `with open(...)` better than just `open(...)`?",
            "options": ["It reads faster", "It automatically closes the file", "It fixes spelling errors", "It uses less RAM"],
            "answer": "It automatically closes the file"
        }
    ]

    # --- QUIZ FORM LOGIC ---
    score = 0
    user_answers = {}

    # We use st.form so the page doesn't reload on every click
    with st.form("quiz_form"):
        for i, q in enumerate(quiz_data):
            st.subheader(q["question"])
            # Create a radio button for each question
            user_answers[i] = st.radio(
                f"Select answer for Q{i+1}:", 
                q["options"], 
                key=f"q{i}", 
                index=None # No default selection
            )
            st.write("---")
        
        # Submit Button
        submitted = st.form_submit_button("Submit Final Exam")

    # --- RESULT CALCULATION ---
    if submitted:
        # Check answers
        for i, q in enumerate(quiz_data):
            if user_answers[i] == q["answer"]:
                score += 1
        
        # Calculate Percentage
        total_questions = len(quiz_data)
        percentage = int((score / total_questions) * 100)

        # Loading animation
        with st.spinner('Checking your answers...'):
            time.sleep(1.5)

        # Show Results
        st.balloons() if percentage == 100 else None
        
        st.metric(label="Your Score", value=f"{score}/{total_questions}", delta=f"{percentage}%")

        if percentage == 100:
            st.success("🏆 LEGENDARY! Perfect Score. You have mastered Season 1.")
        elif percentage >= 65:
            st.success("✅ PASSED! You have a solid foundation🗿.")
        else:
            st.error("❌ FAILED🥲. You need more practice.")
            st.write("It is recommended to re-watch 👀😈🤧")

        # Show Answer Key (Optional - expands if clicked)
        with st.expander("View Correct Answers"):
            for i, q in enumerate(quiz_data):
                st.write(f"**Q{i+1}:** {q['question']}")
                st.write(f"✅ Correct Answer: `{q['answer']}`")
                st.write("---")

# Run the app
if __name__ == "__main__":
    main()
