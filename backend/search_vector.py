from sentence_transformers import SentenceTransformer
import psycopg2
import numpy as np

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="vector_tasks",
    user="postgres",
    password="bangtan",  
    host="localhost",
    port=5432
)
cur = conn.cursor()

# Load the same model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Input query
query = "What is this task about?"  # You can change this
embedding = model.encode(query)

# Convert to tuple and CAST to vector for pgvector
cur.execute("""
    SELECT description, embedding <#> %s::vector AS distance
    FROM tasks
    ORDER BY distance ASC
    LIMIT 5
""", (embedding.tolist(),))  # <- ensure it's a 1-tuple

# Fetch and display results
results = cur.fetchall()

print("\n🔍 Top Similar Results:")
for row in results:
    print(f"• {row[0]} (distance: {row[1]:.4f})")

cur.close()
conn.close()

