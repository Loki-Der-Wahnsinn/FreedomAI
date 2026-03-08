from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import List, Dict
import uvicorn
from core.commander import Commander

app = FastAPI(title="FreedomAI Command Center")
commander = Commander()

class CommandRequest(BaseModel):
    command: str

@app.get("/")
def get_status():
    return {
        "status": "ONLINE",
        "teams": list(commander.teams.keys()),
        "agents_active": sum(len(team.agents) for team in commander.teams.values()),
        "memory_shards": 124, # Simulated
        "singularity_factor": 0.98 # Simulated
    }

@app.get("/teams")
def get_teams():
    return {name: [agent.name for agent in team.agents] for name, team in commander.teams.items()}

@app.post("/issue-command")
def issue_command(req: CommandRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(commander.issue_command, req.command)
    return {"status": "Command received and delegated", "command": req.command}

if __name__ == "__main__":
    # Auto-initialize some teams for display
    commander.create_team("Hyperion-Core", ["Agent-Alpha", "Agent-Beta"])
    commander.create_team("Shadow-Net", ["Agent-Gamma", "Agent-Delta"])
    uvicorn.run(app, host="0.0.0.0", port=8080)
