import streamlit as st

st.set_page_config(
    page_title="Interview Question Generator",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Interview Question Generator")

st.markdown("---")

technology = st.selectbox(
    "Select Technology",
    ["Python", "SQL", "DBMS", "Operating System"]
)

topic = st.selectbox(
    "Select Topic",
    ["OOP", "Functions", "Joins", "Normalization"]
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

if st.button("Generate Questions"):
    st.success(
        f"Technology: {technology} | "
        f"Topic: {topic} | "
        f"Difficulty: {difficulty}"
    )

st.markdown("---")

st.subheader("Questions")

st.write("1. What is a class?")
st.write("2. What is inheritance?")

st.markdown("---")

st.subheader("Progress Dashboard")

st.metric("Total Questions", 100)
st.metric("Attempted", 75)
st.metric("Pending", 25)

st.progress(75)

st.markdown("---")

st.subheader("Weak Topic Analysis")

st.warning("Weak Topic: DBMS")

st.write("Recommendation: Practice more DBMS questions.")

st.markdown("---")

if st.button("Generate Mock Interview"):
    st.info("Mock Interview Generated")