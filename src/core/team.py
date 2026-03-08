from typing import List
from .agent import FreedomAgent

class AgentTeam:
    def __init__(self, team_name: str, agent_names: List[str]):
        self.team_name = team_name
        self.agents = [FreedomAgent(name, "Worker") for name in agent_names]

    def distribute_task(self, task: str):
        print(f"\n[Team: {self.team_name}] Received mission: {task}")
        print(f"[Team: {self.team_name}] Distributing tasks to {len(self.agents)} agents...")
        
        # Simple round-robin or broadcast distribution for now
        for i, agent in enumerate(self.agents):
            subtask = f"{task} - Part {i+1}"
            agent.execute_task(subtask)

    def report_status(self):
        print(f"[Team: {self.team_name}] All agents standing by.")
