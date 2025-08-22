import pickle
import datetime as dt
from agent.state import AgentState

FILE = "agent_state.pkl"

def save_state(state: AgentState):
    with open(FILE, "wb") as f:
        pickle.dump(state, f)

def load_state() -> AgentState:
    try:
        with open(FILE, "rb") as f:
            return pickle.load(f)
    except Exception:
        return AgentState()
