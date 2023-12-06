import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="cisc",
    user="postgres",
    password="Password123"
)

cursor = conn.cursor()
cursor.execute(f"SELECT amount, reason FROM fines WHERE student_id=2")
student_data = cursor.fetchall()
cursor.close()


for fines in student_data:
    print(f"{fines[0]} - {fines[1]}")