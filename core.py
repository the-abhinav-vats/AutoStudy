import datetime as dt
from .state import AgentState, StudyTask, QuizItem
from .utils import chunk_list, random_question

def build_plan(state: AgentState, blocks_per_day=6):
    if not state.syllabus or not state.deadline:
        return []

    today = dt.date.today()
    days_left = (state.deadline - today).days
    total_blocks = days_left * blocks_per_day

    if total_blocks <= 0:
        return []

    chunks = chunk_list(state.syllabus, total_blocks)
    tasks = []
    block_index = 0
    for day_offset in range(days_left):
        for block in range(blocks_per_day):
            if block_index < len(chunks):
                tasks.append(
                    StudyTask(
                        chunks[block_index][0],
                        today + dt.timedelta(days=day_offset),
                        block,
                    )
                )
                block_index += 1
    state.tasks = tasks
    return tasks


def generate_quiz(state: AgentState):
    if not state.syllabus:
        return []

    state.quizzes = [QuizItem(random_question(topic), f"Explanation of {topic}") for topic in state.syllabus]
    return state.quizzes
