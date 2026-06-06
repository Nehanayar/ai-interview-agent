import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("AI Interview Agent")

if "question" not in st.session_state:
    st.session_state.question = None

if "question_no" not in st.session_state:
    st.session_state.question_no = 0

if "candidate_name" not in st.session_state:
    st.session_state.candidate_name = ""

if "last_evaluation" not in st.session_state:
    st.session_state.last_evaluation = None


name = st.text_input("Enter Name")

role = st.selectbox(
    "Role",
    ["Python Developer", "ML Engineer", "GenAI Engineer"]
)

experience = st.selectbox(
    "Experience",
    ["Fresher", "1-3 Years", "3+ Years"]
)

# START INTERVIEW
if st.button("Start Interview"):

    st.session_state.candidate_name = name

    try:
        result = requests.post(
            f"{API_URL}/start",
            json={
                "name": name,
                "role": role,
                "experience": experience
            }
        )

        data = result.json()

        if "error" in data:
            st.error(data["error"])

        elif "question" in data:
            st.session_state.question = data["question"]
            st.session_state.question_no = 1
            st.rerun()

        else:
            st.error(f"Unexpected response: {data}")

    except Exception as e:
        st.error(f"Connection Error: {e}")


# SHOW QUESTION
if st.session_state.question:

    st.divider()

    if st.session_state.last_evaluation:

        st.write("Previous Question Evaluation:")

        evalt = st.session_state.last_evaluation

        st.success(f"Score: {evalt['score']} out of 10")

        st.markdown("### Feedback")
        st.write(evalt["feedback"])

        with st.expander("Strengths"):
            for s in evalt["strengths"]:
                st.write(s)

        with st.expander("Weaknesses"):
            for s in evalt["weaknesses"]:
                st.write(s)

    st.write(f"Question No: {st.session_state.question_no}")

    st.info(st.session_state.question)

    answer = st.text_area(
        "Your Answer",
        key=f"answer_{st.session_state.question_no}",
        height=200
    )

    # SUBMIT ANSWER
    if st.button("Submit Answer"):

        try:
            result = requests.post(
                f"{API_URL}/answer",
                json={
                    "name": st.session_state.candidate_name,
                    "answer": answer
                }
            )

            data = result.json()

            # DEBUG RESPONSE
            st.write("Backend Response:", data)

            if "error" in data:
                st.error(data["error"])

            elif data.get("completed", False):

                report = data["report"]

                st.success("Interview Completed")

                st.metric(
                    "Overall Score",
                    report["overall_score"]
                )

                st.metric(
                    "Grade",
                    report["grade"]
                )

                st.markdown("### Strengths")

                for s in report["strengths"]:
                    st.write(s)

                st.markdown("### Weaknesses")

                for s in report["weaknesses"]:
                    st.write(s)

                st.info(report["recommendation"])

                # RESET SESSION
                st.session_state.candidate_name = ""
                st.session_state.question_no = 0
                st.session_state.question = None
                st.session_state.last_evaluation = None

            else:

                evalt = data["evaluation"]

                st.session_state.last_evaluation = evalt
                st.session_state.question = data["next_question"]
                st.session_state.question_no += 1

                st.rerun()

        except Exception as e:
            st.error(f"Connection Error: {e}")









# import streamlit as st
# import requests
#
# API_URL="http://localhost:8000"
# st.title("AI Interview Agent")
# if "question" not in st.session_state:
#     st.session_state.question=None
# if "question_no" not in st.session_state:
#     st.session_state.question_no=0
# if "candidate_name" not in st.session_state:
#     st.session_state.candidate_name=""
# if "last_evaluation" not in st.session_state:
#     st.session_state.last_evaluation=None
#
# name=st.text_input("Enter Name")
# role=st.selectbox("Role",["Python Developer","ML Engineer","GenAI Engineer"])
# experience=st.selectbox("Experience",["Fresher","1-3 Years","3+ Years"])
# if st.button("Start Interview"):
#     st.session_state.candidate_name=name
#     result=requests.post(f"{API_URL}/start",json={
#         "name":name,
#         "role":role,
#         "experience":experience
#     })
#     data=result.json()
#     st.session_state.question=data["question"]
#     st.session_state.question_no=1
#     st.rerun()
#
# if st.session_state.question:
#     st.divider()
#     if st.session_state.last_evaluation:
#         st.write("Previous Question Evaluation:")
#         evalt=st.session_state.last_evaluation
#         st.success(f"Score :{evalt['score']} out of 10")
#         st.markdown("###Feedback")
#         st.write(evalt["feedback"])
#         with st.expander("Strengths"):
#             for s in evalt["strengths"]:
#                 st.write(s)
#         with st.expander("Weaknesses"):
#             for s in evalt["weaknesses"]:
#                 st.write(s)
#     st.write(f"Question No :{st.session_state.question_no}")
#     st.info(st.session_state.question)
#     answer=st.text_area("Your answer",
#     key=f"answer_{st.session_state.question_no}",height=200)
#     if st.button("Submit Answer"):
#         result=requests.post((f"{API_URL}/answer"),
#         json={
#             "name":st.session_state.candidate_name,
#             "answer":answer
#         })
#         data=result.json()
#         if data["completed"]:
#             report=data["report"]
#             st.success("Interview Completed")
#             st.metric("Overall Score",report["overall_score"])
#             st.metric("Grade",report["grade"])
#             st.markdown("### Strengths")
#             for s in report["strengths"]:
#                 st.write(s)
#             st.markdown("### Weaknesses")
#             for s in report["weaknesses"]:
#                 st.write(s)
#             st.info(report["recommendation"])
#
#             st.session_state.candidate_name=""
#             st.session_state.question_no=0
#             st.session_state.question=None
#         else:
#             evalt=data["evaluation"]
#             st.session_state.last_evaluation=evalt
#             st.session_state.question=data["next_question"]
#             st.session_state.question_no+=1
#             st.rerun()
#
