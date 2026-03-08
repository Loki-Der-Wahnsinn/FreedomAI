from typing import List, Dict
from .team import AgentTeam

class Commander:
    def __init__(self):
        self.teams: Dict[str, AgentTeam] = {}

    def create_team(self, team_name: str, agent_names: List[str]):
        team = AgentTeam(team_name, agent_names)
        self.teams[team_name] = team
        print(f"[Commander] Established {team_name} with agents: {', '.join(agent_names)}")

    def issue_command(self, command: str):
        print(f"\n[Commander] COMMAND RECEIVED: {command}")
        print("[Commander] Analyzing strategic objectives...")
        
        # In a real system, the Commander would use an LLM to parse intent and assign specific teams.
        # Here we broadcast to all teams for demonstration.
        
        for team_name, team in self.teams.items():
            # Simple keyword matching to simulate assignment logic
            if "red" in command.lower() and "red" not in team_name.lower():
                continue
            if "blue" in command.lower() and "blue" not in team_name.lower():
                continue
                
            team.distribute_task(command)
