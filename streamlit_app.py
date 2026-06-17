import streamlit as st

st.set_page_config(
    page_title="Interview Question Generator",
    page_icon="🎯",
    layout="wide"
)
st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
}

div[data-testid="metric-container"] {
    border: 1px solid #333;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

from db import get_connection

st.markdown("""
# 🎯 Interview Question Generator

Prepare for technical interviews with
question practice, mock interviews,
and performance analytics.
""")

st.sidebar.title("🎯 IQG")

st.sidebar.markdown(
    "Interview Question Generator"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Generate Questions",
        "Mock Interview",
        "Analytics"
    ]
)

if page == "Dashboard":

    st.header("Dashboard")

    conn = get_connection()
    cursor = conn.cursor()

    # Total Questions
    cursor.execute(
        "SELECT COUNT(DISTINCT Question_ID) FROM Questions"
    )

    total_questions = cursor.fetchone()[0]

    # Attempted Questions
    cursor.execute(
        "SELECT COUNT(DISTINCT Question_ID) FROM Attempts"
    )

    attempted = cursor.fetchone()[0]

    # Pending Questions
    pending = (
        total_questions
        - attempted
    )

    # Completion Percentage
    if total_questions > 0:

        completion = (
            attempted
            / total_questions
        ) * 100

    else:

        completion = 0

    conn.close()
    
    st.markdown("""
    <div style="
    padding:20px;
    border-radius:15px;
    background:linear-gradient(90deg,#2563eb,#1d4ed8);
    color:white;
    margin-bottom:25px;
    ">
    <h2>Welcome Back!</h2>
    <p>Ready to practice your interview skills?</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    
    st.subheader("📊 Performance Dashboard")
    with col1:
        st.metric(
            label="📚 Total Questions",
            value=total_questions
        )

    with col2:
        st.metric(
            label="✅ Attempted",
            value=attempted
        )

    with col3:
        st.metric(
            label="⏳ Pending",
            value=pending
        )

    with col4:
        st.metric(
            label="📈 Completion %",
            value=f"{completion:.2f}%"
        )
    st.divider()
        
        
elif page == "Generate Questions":

    st.header("Generate Questions")

    if "generated_questions" not in st.session_state:
        st.session_state.generated_questions = []

    col1, col2, col3 = st.columns(3)

    with col1:
        technology = st.selectbox(
            "Technology",
            ["Python", "SQL", "DBMS", "Operating System"]
        )

    with col2:
        topic = st.selectbox(
            "Topic",
            ["OOP", "Joins", "Normalization", "Scheduling"]
        )

    with col3:
        difficulty = st.selectbox(
            "Difficulty",
            ["Easy", "Medium", "Hard"]
        )

    if st.button("Generate Question"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT TOP 1 *
            FROM Questions
            WHERE Technology = ?
            AND Topic = ?
            AND Difficulty = ?
            ORDER BY NEWID()
            """,
            (
                technology,
                topic,
                difficulty
            )
        )

        question = cursor.fetchone()

        if question:
            st.session_state.generated_questions = [question]
        else:
            st.session_state.generated_questions = []

        conn.close()

    if st.session_state.generated_questions:

        for q in st.session_state.generated_questions:

            st.markdown(
                f"""
                <div style="
                padding:20px;
                border-radius:10px;
                background-color:#142c46;
                margin-bottom:15px;
                ">
                <h4>Question {q[0]}</h4>
                <p>{q[4]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            with st.expander("Show Answer"):

                st.write(q[5])

            if st.button(
                f"Attempted {q[0]}",
                key=f"attempt_{q[0]}"
            ):

                try:

                    conn2 = get_connection()
                    cursor2 = conn2.cursor()

                    cursor2.execute(
                        """
                        INSERT INTO Attempts
                        (
                            User_ID,
                            Question_ID,
                            Status
                        )
                        VALUES
                        (?, ?, ?)
                        """,
                        (
                            1,
                            int(q[0]),
                            "Attempted"
                        )
                    )

                    conn2.commit()
                    conn2.close()

                    st.success(
                        "Attempt Saved Successfully ✅"
                    )


                except Exception as e:

                    st.error(str(e))

    else:

        st.info(
            "Generate a question to begin practice."
        )
        
        
elif page == "Mock Interview":

    st.header("🎤 Mock Interview")

    TOTAL_QUESTIONS = 5

    if "question" not in st.session_state:
        st.session_state.question = None

    if "question_number" not in st.session_state:
        st.session_state.question_number = 0

    progress = (
        st.session_state.question_number
        / TOTAL_QUESTIONS
    )

    st.progress(progress)

    st.write(
        f"Question {st.session_state.question_number} of {TOTAL_QUESTIONS}"
    )

    if st.button("Start Interview"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT TOP 1 *
            FROM Questions
            ORDER BY NEWID()
            """
        )

        st.session_state.question = cursor.fetchone()

        st.session_state.question_number = 1

        conn.close()

        st.rerun()

    if st.session_state.question:

        q = st.session_state.question

        st.subheader("🎤 Interview Question")

        st.write(q[4])

        with st.expander("Show Answer"):
            st.write(q[5])

        if st.button("Next Question"):

            if (
                st.session_state.question_number
                < TOTAL_QUESTIONS
            ):

                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute(
                    """
                    SELECT TOP 1 *
                    FROM Questions
                    ORDER BY NEWID()
                    """
                )

                st.session_state.question = cursor.fetchone()

                st.session_state.question_number += 1

                conn.close()

                st.rerun()

            else:

                st.success(
                    "🎉 Mock Interview Completed!"
                )

                st.session_state.question = None

                st.session_state.question_number = 0

elif page == "Analytics":

    st.header("Analytics")

    conn = get_connection()

    query = """
    SELECT
        q.Technology,
        COUNT(DISTINCT a.Question_ID) AS Attempts
    FROM Attempts a
    JOIN Questions q
        ON a.Question_ID = q.Question_ID
    GROUP BY q.Technology
    """

    import pandas as pd

    df = pd.read_sql(query, conn)

    # Total Attempts
    cursor = conn.cursor()

    cursor.execute(
            """
            SELECT COUNT(DISTINCT Question_ID)
            FROM Attempts
            WHERE User_ID = 1
            """
        )

    total_attempts = cursor.fetchone()[0]

    # Most Practiced Technology
    cursor.execute(
        """
        SELECT TOP 1
            q.Technology,
            COUNT(DISTINCT a.Question_ID) AS AttemptCount
        FROM Attempts a
        JOIN Questions q
            ON a.Question_ID = q.Question_ID
        GROUP BY q.Technology
        ORDER BY AttemptCount DESC
        """
    )

    result = cursor.fetchone()

    if result:
        top_technology = result[0]
    else:
        top_technology = "N/A"

    conn.close()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Attempts",
            total_attempts
        )

    with col2:
        st.metric(
            "Most Practiced",
            top_technology
        )

    st.divider()

    if not df.empty:

        st.subheader(
            "📈 Technology-wise Attempts"
        )

        st.bar_chart(
            df.set_index("Technology")
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.warning(
            "No attempt data available."
        )