# from typing import TypedDict, List
# from dotenv import load_dotenv
# from pydantic import BaseModel
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langgraph.graph import StateGraph
# import os
#
# # Load environment variables
# load_dotenv()
#
# # Check API Key
# api_key = os.getenv("GEMINI_API_KEY")
#
# if not api_key:
#     raise ValueError("GEMINI_API_KEY not found in .env file")
#
# print("Gemini Key Loaded Successfully")
#
# # LLM
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=api_key,
#     temperature=0.3
# )
#
#
# # =========================
# # STATE
# # =========================
#
# class InterviewState(TypedDict):
#     role: str
#     experience: str
#     question_no: int
#     history: List[dict]
#     current_question: str
#
#
# # =========================
# # QUESTION GENERATION
# # =========================
#
# def generate_question(state):
#
#     try:
#         previous_questions = [
#             item.get("question", "")
#             for item in state.get("history", [])
#         ]
#
#         prompt = f"""
# Generate interview question number {state["question_no"]}
#
# Role:
# {state["role"]}
#
# Experience:
# {state["experience"]}
#
# Focus Areas:
# - Python
# - Machine Learning
# - Deep Learning
# - Generative AI
#
# Previous Questions:
# {previous_questions}
#
# Rules:
# 1. Do not repeat previous questions
# 2. Ask only one question
# 3. Return only the question text
# """
#
#         response = llm.invoke(prompt)
#
#         question = (
#             response.content.strip()
#             if response.content
#             else "Tell me about yourself."
#         )
#
#         state["current_question"] = question
#
#         return state
#
#     except Exception as e:
#
#         print("QUESTION GENERATION ERROR:", str(e))
#
#         state["current_question"] = (
#             f"Unable to generate question. Error: {str(e)}"
#         )
#
#         return state
#
#
# # =========================
# # EVALUATION MODEL
# # =========================
#
# class Evaluation(BaseModel):
#     score: int
#     strengths: List[str]
#     weaknesses: List[str]
#     feedback: str
#
#
# class InterviewReport(BaseModel):
#     overall_score: int
#     grade: str
#     strengths: List[str]
#     weaknesses: List[str]
#     recommendation: str
#
#
# evaluation_llm = llm.with_structured_output(Evaluation)
# report_llm = llm.with_structured_output(InterviewReport)
#
#
# # =========================
# # ANSWER EVALUATION
# # =========================
#
# def evaluate_answer(question, answer):
#
#     try:
#
#         prompt = f"""
# You are a technical interviewer.
#
# Question:
# {question}
#
# Candidate Answer:
# {answer}
#
# Evaluate the answer.
#
# Return:
# 1. score out of 10
# 2. strengths
# 3. weaknesses
# 4. feedback
# """
#
#         result = evaluation_llm.invoke(prompt)
#
#         return result.model_dump()
#
#     except Exception as e:
#
#         print("EVALUATION ERROR:", str(e))
#
#         return {
#             "score": 0,
#             "strengths": [],
#             "weaknesses": ["Evaluation failed"],
#             "feedback": str(e)
#         }
#
#
# # =========================
# # FINAL REPORT
# # =========================
#
# def generate_report(history):
#
#     try:
#
#         prompt = f"""
# Interview History:
#
# {history}
#
# Generate final interview report.
#
# Include:
# - overall score out of 20
# - grade
# - strengths
# - weaknesses
# - hiring recommendation
# """
#
#         result = report_llm.invoke(prompt)
#
#         return result.model_dump()
#
#     except Exception as e:
#
#         print("REPORT ERROR:", str(e))
#
#         return {
#             "overall_score": 0,
#             "grade": "Failed",
#             "strengths": [],
#             "weaknesses": ["Report generation failed"],
#             "recommendation": str(e)
#         }
#
#
# # =========================
# # LANGGRAPH
# # =========================
#
# builder = StateGraph(InterviewState)
#
# builder.add_node(
#     "generate_question",
#     generate_question
# )
#
# builder.set_entry_point(
#     "generate_question"
# )
#
# graph = builder.compile()
#
#
#











from typing import TypedDict,List
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3
)

class InterviewState(TypedDict):
    role:str
    experience:str
    question_no:int
    history:List[dict]
    current_question:str

def generate_question(state):
    prv_qst = [item.get("question", "") for item in state.get("history", [])]
    prompt=f"""
Generate interview question number {state["question_no"]}.
Role:
{state["role"]}
Experience:
{state["experience"]}
Focus on:
-Python
-Machine Learning
-Deep Learning
-Generative AI
Previous Questions:
{prv_qst}
Rules:
-Do not repeat previous question
-Return only the question
"""
    response=llm.invoke(prompt)
    state["current_question"]=response.content
    return state

from pydantic import BaseModel
class Evaluation(BaseModel):
    score:int
    strengths:List[str]
    weaknesses:List[str]
    feedback:str

class InterviewReport(BaseModel):
    overall_score:int
    grade:str
    strengths: List[str]
    weaknesses: List[str]
    recommendation: str

evaluation_llm=llm.with_structured_output(Evaluation)
report_llm=llm.with_structured_output(InterviewReport)

def evaluate_answer(question,answer):
    prompt=f"""
You are a technical interviewer.
Question:
{question}
Candidate's Answer:
{answer}
Evaluate the answer.
Give:
1.score out of 10
2.strengths
3.weaknesses
4.feedback
"""
    result=evaluation_llm.invoke(prompt)
    return result.model_dump()

def generate_report(history):
    prompt=f"""
Interview History
{history}

Generate final interview report.
Include:
-overall score out of 20
-grade
-strengths
-weaknesses
-hiring recommendation
"""
    result=report_llm.invoke(prompt)
    return result.model_dump()

from langgraph.graph import StateGraph
builder=StateGraph(InterviewState)
builder.add_node("generate_question",generate_question)
builder.set_entry_point("generate_question")
graph=builder.compile()
