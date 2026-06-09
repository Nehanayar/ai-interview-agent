# 🤖 AI Interview Agent

An AI-powered Interview Agent that conducts technical interviews, evaluates candidate answers, and generates detailed performance reports.

---

🌐 Live Demo

🚀 Try the application here:

https://your-streamlit-app.streamlit.app

Note: The application uses Google Gemini API. The demo may be temporarily unavailable if the free API quota limit is reached.


## 🚀 Features

✅ AI-generated interview questions

✅ Role-based interviews

* Python Developer
* ML Engineer
* GenAI Engineer

✅ Answer evaluation with scoring

✅ Strength and weakness analysis

✅ Final interview report generation

✅ FastAPI backend

✅ Streamlit frontend

✅ LangGraph workflow

✅ Gemini AI integration

✅ SQLite database support

---

## 🛠 Tech Stack

| Technology    | Purpose                             |
| ------------- | ----------------------------------- |
| Python        | Core Programming                    |
| FastAPI       | Backend API                         |
| Streamlit     | Frontend UI                         |
| LangGraph     | Interview Workflow                  |
| Google Gemini | AI Question Generation & Evaluation |
| SQLite        | Database                            |
| SQLAlchemy    | ORM                                 |

---

## 📂 Project Structure

```text
ai-interview-agent/
│
├── Backend/
│   ├── main.py
│   ├── graph.py
│   ├── database.py
│   └── model.py
│
├── Frontend/
│   └── streamlitapp.py
│
├── Screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ai-interview-agent.git
cd ai-interview-agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

```env
GEMINI_API_KEY=your_api_key
```

### Run Backend

```bash
uvicorn Backend.main:app --reload
```

### Run Frontend

```bash
streamlit run Frontend/streamlitapp.py
```

---

## 📸 Screenshots

### Home Page

![Home Page](Screenshots/Screenshot%202026-06-06%20152030.png)

### Interview Page

![Interview Page](Screenshots/Screenshot%202026-06-06%20152106.png)

### Final Report

![Final Report](Screenshots/Screenshot%202026-06-06%20152135.png)

---

## ⚙️ How It Works

1. Candidate enters personal and interview details.
2. AI generates role-specific interview questions.
3. Candidate submits answers through the Streamlit interface.
4. Gemini AI evaluates each response.
5. The system provides scores, strengths, weaknesses, and feedback.
6. A final interview report is generated.

---

## ⭐ Key Highlights

* Built an AI-powered interview automation system.
* Integrated Google Gemini for intelligent answer evaluation.
* Implemented LangGraph workflow for interview management.
* Developed a FastAPI backend and Streamlit frontend.
* Generated detailed candidate performance reports.
* Designed a scalable architecture for multiple technical roles.

---

## 👩‍💻 Author

**Neha Nayar**
