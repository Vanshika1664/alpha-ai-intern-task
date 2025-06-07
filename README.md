# Alpha AI Intern Task

This repository contains the full-stack implementation of the Alpha AI intern task. It includes:

- ✅ Frontend: React
- ✅ Backend: Flask
- ✅ Vector Search with PostgreSQL + pgvector
- ✅ Sentence Embeddings using `sentence-transformers`

---

## 🚀 Features

- Add and manage tasks via UI
- Search similar tasks using vector similarity
- Cache and refresh mechanism for syncing backend state
- Full integration with PostgreSQL vector search using pgvector

---

## 📂 Project Structure

alpha-ai-intern-task/
├── backend/ # Flask backend
│ ├── app.py
│ ├── search_vector.py
│ ├── check_tasks.py
│ ├── dockerfile
│ ├── requirements.txt
│ └── insert_vector.py
├── frontend/ # React frontend
│ └── src/
│ ├── App.js
│ ├── App.test.js
│ ├── index.js
│ ├── index.css
│ ├── logo.svg
│ ├── reportWebVitals.js
│ └── setupTests.js
├── my-frontend

---

## 🛠️ Setup Instructions

### 🧠 Backend (Flask + PostgreSQL + pgvector)

1. **Install Python dependencies:**

   ```bash
   pip install -r backend/requirements.txt
2. Run the backend server:
   python backend/app.py

3. PostgreSQL setup:
   Make sure PostgreSQL is installed and running
   Install the pgvector extension:
   CREATE EXTENSION IF NOT EXISTS vector;
   Create a table with a vector column
   Use sentence-transformers to convert tasks into embeddings and insert them into the database

4. Install frontend dependencies:
   cd frontend
   npm install

5. Run the frontend app:
   npm start

🧰 Technologies Used
  1. React
  2. Flask
  3. PostgreSQL + pgvector
  4. sentence-transformers
  5. GitHub

🙋‍♀️ Author
Vanshika Tomar

