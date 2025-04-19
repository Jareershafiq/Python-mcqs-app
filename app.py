import streamlit as st

# ---- Light Pink Theme via HTML & CSS ----
def set_custom_theme():
    st.markdown("""
        <style>
            body {
                background-color: #ffe6f0;
                color: #000000;
            }
            .stApp {
                background-color: #fff0f5;
                color: #000000;
            }
            h1, h2, h3, h4, h5, h6, p, label, div {
                color: #0000FF !important;
            }
            .css-1cpxqw2 {
                color: #000000 !important;
            }
            /* Input fields, select box, multiselect, and checkboxes */
            .stTextInput input, .stMultiselect div, .stSelectbox select, .stCheckbox input {
                color: white;  /* Text color inside the boxes */
                background-color: #cc0066;  /* Box background color */
            }
            .stTextInput input:focus, .stMultiselect div:focus, .stSelectbox select:focus, .stCheckbox input:focus {
                border-color: #ff66b3;  /* Border color when focused */
            }
            /* Button "Let's Begin" color */
            .stButton button {
                background-color: #ff66b3;
                color: white;
                font-weight: bold;
                border-radius: 5px;
            }
            .stButton button:hover {
                background-color: #cc0066;
            }
            /* Footer */
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: #cc0066;
                color: white;
                text-align: center;
                padding: 10px;
                font-size: 16px;
                font-family: 'Arial', sans-serif;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            }
            .footer a {
                color: #ffffff;
                text-decoration: none;
                font-weight: bold;
            }
            .footer a:hover {
                text-decoration: underline;
            }
        </style>
    """, unsafe_allow_html=True)

# ---- Questions Database ----
mcqs = {
    "Basic": [
        {
            "question": "Which are valid Python keywords?",
            "options": ["if", "then", "else", "elif"],
            "answer": ["if", "else", "elif"]
        },
        {
            "question": "Which of these are loops in Python?",
            "options": ["for", "while", "loop", "repeat"],
            "answer": ["for", "while"]
        },
        # Add 28 more Basic questions...
    ],
    "Intermediate": [
        {
            "question": "Which are valid list methods?",
            "options": ["append()", "add()", "extend()", "insert()"],
            "answer": ["append()", "extend()", "insert()"]
        },
        {
            "question": "What are Python exception types?",
            "options": ["ValueError", "TypeError", "WrongError", "SyntaxError"],
            "answer": ["ValueError", "TypeError", "SyntaxError"]
        },
        # Add 28 more Intermediate questions...
    ],
    "Advanced": [
        {
            "question": "Which of the following are valid decorators?",
            "options": ["@staticmethod", "@classmethod", "@wraps", "@jsonify"],
            "answer": ["@staticmethod", "@classmethod", "@wraps"]
        },
        {
            "question": "Which modules are in Python's standard library?",
            "options": ["os", "json", "pandas", "re"],
            "answer": ["os", "json", "re"]
        },
        # Add 28 more Advanced questions...
    ]
}

# ---- Session State Init ----
if 'username' not in st.session_state:
    st.session_state.username = None
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'level_selected' not in st.session_state:
    st.session_state.level_selected = False

# ---- Set Theme ----
set_custom_theme()

# ---- Login Page ----
if not st.session_state.authenticated:
    st.title("🧠 Python MCQs Quiz Login")
    name = st.text_input("👤 Enter your name")
    password = st.text_input("🔒 Enter password", type="password")
    if st.button("Let's Begin"):
        if name.strip() != "" and password.strip() != "":
            st.session_state.username = name.strip().title()
            st.session_state.authenticated = True
            st.success(f"Welcome, {st.session_state.username}! Let's test your Python skills.")
        else:
            st.warning("Please enter both name and password to continue.")

# ---- Level Selection ----
elif not st.session_state.level_selected:
    st.title(f"👋 Welcome {st.session_state.username}")
    st.subheader("📚 Choose your difficulty level:")
    level = st.selectbox("Select Level:", ["Basic", "Intermediate", "Advanced"])
    if st.button("Start Quiz"):
        st.session_state.selected_level = level
        st.session_state.level_selected = True

# ---- Quiz Page ----
else:
    level = st.session_state.selected_level
    questions = mcqs[level]
    score = 0
    user_answers = []

    st.title(f"🎯 {level} Level Quiz for {st.session_state.username}")
    with st.form("quiz_form"):
        for i, q in enumerate(questions):
            st.markdown(f"**Q{i+1}: {q['question']}**")
            selected = st.multiselect("Select answer(s):", q["options"], key=f"q_{i}")
            user_answers.append((selected, q["answer"]))
        submitted = st.form_submit_button("Submit Quiz")

    if submitted:
        for selected, correct in user_answers:
            if set(selected) == set(correct):
                score += 1
        st.success(f"🎉 {st.session_state.username}, you scored {score} out of {len(questions)}!")

# ---- Stylish Footer ----
st.markdown("""
    <div class="footer">
        Made by <a href="https://www.linkedin.com/in/jareer-shafiq" target="_blank">Jareer Shafiq</a>
    </div>
""", unsafe_allow_html=True)
