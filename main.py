import streamlit as st
from agent.state import AgentState
from agent import core
from ui import plan_tab, quiz_tab, explain_tab, review_tab
from storage import persistence

st.set_page_config(page_title="AutoStudy Coach", page_icon="📚", layout="wide")
st.title("📚 AutoStudy Coach — Autonomous Study Planner & Tutor")

# ----------- State Management -----------
if "agent_state" not in st.session_state:
    st.session_state.agent_state = persistence.load_state()

state: AgentState = st.session_state.agent_state

# ----------- Sidebar Inputs -----------
with st.sidebar:
    st.header("Setup")
    state.deadline = st.date_input("Exam/Goal Deadline", value=state.deadline)
    state.blocks_per_day = st.slider("Study blocks/day (25 min each)", 2, 12, state.blocks_per_day)
    syllabus_input = st.text_area("Syllabus topics (one per line)", value="\n".join(state.syllabus))

    if syllabus_input:
        state.syllabus = [line.strip() for line in syllabus_input.splitlines() if line.strip()]

# ----------- Tabs -----------
tab1, tab2, tab3, tab4 = st.tabs(["📅 Plan", "📝 Quiz", "💡 Explain", "🔁 Review"])

with tab1:
    plan_tab.render(state)

with tab2:
    quiz_tab.render(state)

with tab3:
    explain_tab.render(state)

with tab4:
    review_tab.render(state)

# ----------- Save State -----------
persistence.save_state(state)
