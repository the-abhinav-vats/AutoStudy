import streamlit as st
from agent import core

def render(state):
    st.subheader("📖 Topic Explainer")

    if not state.syllabus:
        st.warning("Please add syllabus in the Plan tab first.")
        return

    # ✅ Added unique key
    topic = st.selectbox("Choose topic:", state.syllabus, key="explain_topic_select")

    if st.button("Explain Topic", key="explain_topic_btn"):
        explanation = core.explain_topic(topic)
        st.write("### Explanation")
        st.write(explanation)
