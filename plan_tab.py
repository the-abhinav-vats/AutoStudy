import streamlit as st
from agent import core

def render(state):
    st.subheader("📅 Autonomous Study Plan")

    # Input fields
    syllabus_input = st.text_area("Enter syllabus/topics (comma separated):", key="plan_syllabus_input")
    deadline = st.date_input("Set your deadline:", key="plan_deadline_input")

    if st.button("Save Syllabus & Deadline", key="plan_save_btn"):
        state.syllabus = [s.strip() for s in syllabus_input.split(",") if s.strip()]
        state.deadline = deadline.isoformat()
        st.success("Syllabus and deadline saved!")

    if st.button("Build / Rebuild Plan", key="plan_build_btn"):
        plan = core.build_plan(state, blocks_per_day=6)
        if plan:
            state.plan = plan   # 🔑 store in state
            st.success(
                f"Plan built with {len(plan)} sessions across {len(set(p.date for p in plan))} days."
            )
        else:
            st.warning("Add syllabus topics and a deadline to generate a plan.")

    # Show current plan safely
    if hasattr(state, "plan") and state.plan:
        st.write("### Current Study Plan")
        for task in state.plan:
            st.write(f"📌 **{task.topic}** on {task.date} ({task.duration} min)")
    else:
        st.info("No plan yet. Enter syllabus and build one.")
