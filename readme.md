# Text-to-SQL LLM App

An **end-to-end Text-to-SQL application** built using **LangChain**, **Groq LLM** and **Streamlit**. This tool allows you to convert natural language queries into SQL statements and retrieve results directly from a **SQLite database**.

---

## Features

* **Natural Language to SQL** – Converts plain English into SQL queries using **LLaMA 3.3 (Groq API)**.
* **Secure Database Access** – Connects to a prebuilt `student.db` SQLite database.
* **Interactive UI** – Simple and intuitive interface powered by **Streamlit**.

---

## Project Structure

```
TEXT-SQL-LLM/
│── .env                # Contains your GROQ_API_KEY
│── app.py              # Main Streamlit application
│── database.py         # Script to create & populate the database
│── student.db          # SQLite database file(created after running database.py)
│── readme.md           # Project documentation
│── requirements.txt    # Project requirements file
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Alaaeid2/Text2SQL-LLM.git
cd Text2SQL-LLM
```

### 2. Install Dependencies

**Using pip:**

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_api_key_here
```

### 4. Initialize the Database

```bash
python database.py
```

### 5. Run the Application

```bash
streamlit run app.py
```

Then open the local URL (e.g., **[http://localhost:8501](http://localhost:8501)**) in your browser.

---

## Example Queries

* *"How many students are in the database?"*
* *"List all students in Data Science course."*
* *"Show the names and marks of students in Section A."*
