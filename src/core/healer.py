import traceback
from .llm_provider import LLMProvider

class SelfHealer:
    def __init__(self, llm: LLMProvider):
        self.llm = llm

    def attempt_fix(self, broken_code: str, error_message: str) -> str:
        """
        Analyzes the error and suggests fixed code.
        """
        print(f"[SelfHealer] Analyzing error: {error_message}")
        prompt = f"Fix the following python code which caused an error:\nCODE:\n{broken_code}\n\nERROR:\n{error_message}"
        
        # In a real scenario, the LLM would return improved code.
        # MockLLM captures "fix" in prompt and returns a print statement.
        fixed_code = self.llm.generate_text(prompt)
        
        # Strip markdown code blocks if present (basic cleanup)
        return fixed_code.replace("```python", "").replace("```", "").strip()
