
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
├── app.py
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

Screenshots

Home Page
Screenshot 2026-06-06 152030.png



Interview Page




Final Report



## How It Works

1. Candidate enters personal and interview details.
2. AI generates role-specific interview questions.
3. Candidate submits answers through the Streamlit interface.
4. Gemini AI evaluates each response.
5. The system provides scores, strengths, weaknesses, and feedback.
6. A final interview report is generated.

## Key Highlights

- Built an AI-powered interview automation system.
- Integrated Google Gemini for intelligent answer evaluation.
- Implemented LangGraph workflow for interview management.
- Developed a FastAPI backend and Streamlit frontend.
- Generated detailed candidate performance reports with scoring and recommendations.
- Designed a scalable architecture for multiple technical roles.
