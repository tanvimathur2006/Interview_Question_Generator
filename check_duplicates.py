from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
SELECT
    Technology,
    Topic,
    Difficulty,
    Question,
    COUNT(*) AS DuplicateCount
FROM Questions
GROUP BY
    Technology,
    Topic,
    Difficulty,
    Question
HAVING COUNT(*) > 1
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()