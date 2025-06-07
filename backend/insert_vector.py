from sentence_transformers import SentenceTransformer
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="vector_tasks",
    user="postgres",
    password="bangtan",
    host="localhost",
    port=5432
)
cur = conn.cursor()

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example task descriptions
task_descriptions = [
    "Build a full-stack web application",
    "Implement vector similarity search using pgvector",
    "Clean and analyze a dataset with pandas",
    "Train a neural network using PyTorch",
    "Develop a REST API using Flask"
]

# Insert each with its embedding
for desc in task_descriptions:
    embedding = model.encode(desc).tolist()
    cur.execute(
        "INSERT INTO tasks (description, embedding) VALUES (%s, %s)",
        (desc, embedding)
    )

conn.commit()
cur.close()
conn.close()

print("✅ Sample tasks inserted.")
