from db import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("SELECT DB_NAME()")

result = cursor.fetchone()

print("Connected to:", result[0])

conn.close()