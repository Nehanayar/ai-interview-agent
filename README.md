
# AI Interview Agent

An AI-powered Interview Agent that conducts technical interviews, evaluates candidate answers, and generates detailed performance reports.

## Features

* AI-generated interview questions
* Role-based interviews

  * Python Developer
  * ML Engineer
  * GenAI Engineer
* Answer evaluation with scoring
* Strength and weakness analysis
* Final interview report generation
* FastAPI backend
* Streamlit frontend
* LangGraph workflow
* Gemini AI integration
* SQLite database support

## Tech Stack

* Python
* FastAPI
* Streamlit
* LangGraph
* Google Gemini
* SQLite
* SQLAlchemy

## Installation

```bash
git clone https://github.com/yourusername/ai-interview-agent.git
cd ai-interview-agent

pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

Run Backend:

```bash
uvicorn main:app --reload
```

Run Frontend:

```bash
streamlit run streamlitapp.py
```

## Project Structure

```text
project/
│
├── main.py
├── graph.py
├── model.py
├── database.py
├── streamlitapp.py
├── requirements.txt
├── .env
└── README.md
```

## Author

Neha Nayar
