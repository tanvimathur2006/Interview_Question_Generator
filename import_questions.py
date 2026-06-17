import pandas as pd
from db import get_connection

df = pd.read_csv(
    "questions.csv",
    names=[
        "Technology",
        "Topic",
        "Difficulty",
        "Question",
        "Answer"
    ],
    header=None,
    engine="python",
    on_bad_lines="skip"
)

conn = get_connection()
cursor = conn.cursor()

for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO Questions
        (
            Technology,
            Topic,
            Difficulty,
            Question,
            Answer
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            row["Technology"],
            row["Topic"],
            row["Difficulty"],
            row["Question"],
            row["Answer"]
        )
    )

conn.commit()
conn.close()

print("Questions imported successfully!")