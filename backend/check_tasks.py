import psycopg2

conn = psycopg2.connect(
    dbname="vector_tasks",
    user="postgres",
    password="bangtan",
    host="localhost",
    port=5432
)
cur = conn.cursor()

cur.execute("SELECT description FROM tasks;")
rows = cur.fetchall()

print("\n📦 Existing Records in tasks:")
for row in rows:
    print(f"- {row[0]}")

cur.close()
conn.close()
