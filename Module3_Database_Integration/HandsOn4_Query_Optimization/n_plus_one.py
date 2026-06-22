import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="college_db"
)

cursor = conn.cursor()

print("----- N+1 QUERY VERSION -----")

start = time.time()

cursor.execute("SELECT * FROM enrollments")
enrollments = cursor.fetchall()

queries = 1

for e in enrollments:
    student_id = e[1]

    cursor.execute(
        "SELECT first_name,last_name FROM students WHERE student_id=%s",
        (student_id,)
    )

    cursor.fetchone()
    queries += 1

print("Queries executed:", queries)

print("\n----- JOIN VERSION -----")

cursor.execute("""
SELECT
e.enrollment_id,
s.first_name,
s.last_name
FROM enrollments e
JOIN students s
ON s.student_id=e.student_id
""")

cursor.fetchall()

print("Queries executed: 1")

print("For 10,000 enrollments:")
print("N+1 version = 10,001 queries")
print("JOIN version = 1 query")

end = time.time()

print("Execution time:", end-start)

cursor.close()
conn.close()

