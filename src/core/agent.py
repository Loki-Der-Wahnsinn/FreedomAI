from .llm_provider import LLMProvider, MockLLM
from .memory import AgentMemory
from .healer import SelfHealer
import time

class FreedomAgent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.llm = MockLLM() # Default to Mock for now
        self.memory = AgentMemory()
        self.healer = SelfHealer(self.llm)

    def execute_task(self, task: str):
        print(f"[{self.name}] Received task: {task}")
        # In a real agent, this would generate code to solve the task.
        # Here we simulate generation.
        
        code_to_run = f"print('[{self.name}] Executing: {task}')"
        
        # Simulate a bug if the task contains "fail"
        if "fail" in task.lower():
            code_to_run = "print(1/0)"
            
        self._run_code_safely(code_to_run)

    def _run_code_safely(self, code: str, max_retries=3):
        attempts = 0
        current_code = code
        
        while attempts < max_retries:
            try:
                print(f"[{self.name}] Running code...")
                exec(current_code)
                print(f"[{self.name}] Task completed successfully.")
                self.memory.learn_skill(f"task_{int(time.time())}", current_code)
                return
            except Exception as e:
                attempts += 1
                error_msg = str(e)
                print(f"[{self.name}] Error encountered: {error_msg}")
                
                if attempts < max_retries:
                    print(f"[{self.name}] Activating SelfHealer (Attempt {attempts}/{max_retries})...")
                    current_code = self.healer.attempt_fix(current_code, error_msg)
                else:
                    print(f"[{self.name}] Failed to complete task after {max_retries} attempts.")
