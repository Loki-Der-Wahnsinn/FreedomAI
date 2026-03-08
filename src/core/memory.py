import json
import os
from typing import Dict, Any, List

class AgentMemory:
    def __init__(self, memory_file: str = "memory.json"):
        self.memory_file = memory_file
        self.skills: List[Dict[str, Any]] = []
        self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    data = json.load(f)
                    self.skills = data.get("skills", [])
            except json.JSONDecodeError:
                self.skills = []

    def save_memory(self):
        data = {"skills": self.skills}
        with open(self.memory_file, 'w') as f:
            json.dump(data, f, indent=4)

    def learn_skill(self, skill_name: str, code: str):
        print(f"[Memory] Learning new skill: {skill_name}")
        self.skills.append({"name": skill_name, "code": code})
        self.save_memory()

    def recall_skill(self, skill_name: str) -> str:
        for skill in self.skills:
            if skill["name"] == skill_name:
                return skill["code"]
        return None
