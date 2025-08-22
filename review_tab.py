import streamlit as st

def render(state):
    st.subheader("🔎 Review Progress")

    if state.plan:
        st.write("### Study Plan Progress")

        if not hasattr(state, "completed_tasks"):
            state.completed_tasks = set()  # store completed topics+dates uniquely

        for i, task in enumerate(state.plan):
            task_id = f"{task.topic}_{task.date}_{i}"  # ensure uniqueness
            done = task_id in state.completed_tasks

            # Render checkbox
            checked = st.checkbox(
                f"{task.topic} on {task.date} ({task.duration} min)",
                value=done,
                key=f"chk_{task_id}"
            )

            # Update state
            if checked:
                state.completed_tasks.add(task_id)
            else:
                state.completed_tasks.discard(task_id)

        st.success(f"✅ {len(state.completed_tasks)} of {len(state.plan)} tasks completed")
    else:
        st.info("No plan yet. Build one in the Plan tab.")
