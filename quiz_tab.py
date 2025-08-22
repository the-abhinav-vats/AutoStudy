import streamlit as st
from agent import core

def render(state):
    st.subheader("📝 Practice Quiz")

    if not state.syllabus:
        st.warning("Please add syllabus in the Plan tab first.")
        return

    topic = st.selectbox("Choose topic:", state.syllabus, key="quiz_topic_select")
    if st.button("Generate Quiz", key="quiz_generate_btn"):
        state.current_quiz = core.generate_quiz(topic)
        state.quiz_answers = {}  # reset answers

    if hasattr(state, "current_quiz") and state.current_quiz:
        st.write("### Quiz")

        for i, q in enumerate(state.current_quiz):
            st.write(f"**Q{i+1}: {q['question']}**")
            answer = st.radio(
                f"Choose answer for Q{i+1}",
                q["options"],
                key=f"quiz_q{i}"
            )
            state.quiz_answers[i] = answer

        if st.button("Finish Quiz", key="quiz_finish_btn"):
            score = 0
            weak = []

            for i, q in enumerate(state.current_quiz):
                chosen = state.quiz_answers.get(i)
                if chosen == q["answer"]:
                    score += 1
                else:
                    weak.append(q["topic"])

            st.info(f"Final Score: {score}/{len(state.current_quiz)}")

            if weak:
                st.warning(f"Weak topics: {', '.join(set(weak))}")
                core.update_plan_with_reflection(state, weak)
