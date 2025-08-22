# agent/state.py

from dataclasses import dataclass, field
from typing import List, Optional

# -------------------------
# Study task (schedule)
# -------------------------
@dataclass
class StudyTask:
    topic: str
    date: str
    duration: int
    done: bool = False   # ✅ track progress

# -------------------------
# Quiz item (MCQ / Q&A)
# -------------------------
@dataclass
class QuizItem:
    question: str
    options: List[str]
    answer: str

# -------------------------
# Main agent state
# -------------------------
class AgentState:
    def __init__(self):
        # user inputs
        self.syllabus: List[str] = []
        self.deadline: Optional[str] = None
        self.blocks_per_day: int = 4   # ✅ default study blocks/day

        # generated outputs
        self.plan: List[StudyTask] = []     # study schedule
        self.quiz: List[QuizItem] = []      # quiz questions
        self.notes: List[dict] = []         # explanations / notes
