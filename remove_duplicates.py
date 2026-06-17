from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
SELECT
    Question_ID,
    Technology,
    Topic,
    Difficulty,
    Question
FROM Questions
ORDER BY Question_ID
""")

rows = cursor.fetchall()

seen = set()
deleted = 0

for row in rows:

    key = (
        row.Technology,
        row.Topic,
        row.Difficulty,
        str(row.Question)
    )

    if key in seen:

        cursor.execute(
            """
            DELETE FROM Questions
            WHERE Question_ID = ?
            """,
            row.Question_ID
        )

        deleted += 1

    else:

        seen.add(key)

conn.commit()

print(f"{deleted} duplicate questions removed!")

conn.close()