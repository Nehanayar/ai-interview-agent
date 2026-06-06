
import json

from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal, Base, engine

from Backend.graph import graph, evaluate_answer, generate_report
from Backend.database import SessionLocal
from Backend.model import Interview



Base.metadata.create_all(bind=engine)

app = FastAPI()

sessions = {}


class StartRequest(BaseModel):
    name: str
    role: str
    experience: str


class AnswerRequest(BaseModel):
    name: str
    answer: str


@app.post("/start")
def start(data: StartRequest):
    try:
        state = {
            "role": data.role,
            "experience": data.experience,
            "question_no": 1,
            "history": [],
            "current_question": ""
        }

        result = graph.invoke(state)

        sessions[data.name] = result

        print("SESSION CREATED:", sessions)

        return {
            "question": result["current_question"]
        }

    except Exception as e:
        print("START ERROR:", str(e))

        return {
            "error": str(e)
        }


@app.post("/answer")
def answer(req: AnswerRequest):
    try:

        if req.name not in sessions:
            return {
                "error": "Invalid candidate"
            }

        session = sessions[req.name]

        evaluation = evaluate_answer(
            session["current_question"],
            req.answer
        )

        session["history"].append(
            {
                "question": session["current_question"],
                "answer": req.answer,
                "evaluation": evaluation
            }
        )

        if session["question_no"] >= 2:

            report = generate_report(
                session["history"]
            )

            db = SessionLocal()

            interview = Interview(
                candidate_name=req.name,
                role=session["role"],
                report=json.dumps(report)
            )

            db.add(interview)
            db.commit()
            db.close()

            del sessions[req.name]

            return {
                "completed": True,
                "report": report
            }

        session["question_no"] += 1

        next_state = {
            "role": session["role"],
            "experience": session["experience"],
            "question_no": session["question_no"],
            "history": session["history"],
            "current_question": ""
        }

        result = graph.invoke(next_state)

        session["current_question"] = result["current_question"]

        return {
            "completed": False,
            "question_no": session["question_no"],
            "evaluation": evaluation,
            "next_question": session["current_question"]
        }

    except Exception as e:
        print("ANSWER ERROR:", str(e))

        return {
            "error": str(e)
        }






