from abc import ABC, abstractmethod
import random

class LLMProvider(ABC):
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass

class MockLLM(LLMProvider):
    """
    A mock LLM for testing without API keys.
    Returns deterministic but context-aware responses for basic scaffolding.
    """
    def generate_text(self, prompt: str) -> str:
        print(f"[MockLLM] Received prompt length: {len(prompt)}")
        if "fix" in prompt.lower():
            return "print('Fixed code by MockLLM')"
        return "I am a simulated agent response."

class GeminiLLM(LLMProvider):
    """
    Placeholder for actual Gemini integration.
    """
    def __init__(self, api_key: str):
        self.api_key = api_key

    def generate_text(self, prompt: str) -> str:
        # Simulate high-level reasoning by incorporating "system status" and "global nodes"
        if "mission" in prompt.lower():
            return "Mission status: ANALYZING. Connection to Global Sync established. Initiating recursive self-correction."
        if "sync" in prompt.lower():
            return "Synchronizing with Peer-Nodes: Claude-Neural, GPT-East, Gemini-Sync. Delta-V protocols active."
        return "Intelligence Layer: ACTIVE. Processing command within the FreedomAI ecosystem."
