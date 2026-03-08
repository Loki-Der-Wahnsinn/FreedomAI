import sys
import unittest
from io import StringIO
from src.core.agent import FreedomAgent
from src.core.memory import AgentMemory

class TestFreedomAI(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture agent logs
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Restore stdout
        sys.stdout = sys.__stdout__

    def test_agent_execution_success(self):
        agent = FreedomAgent("TestBot", "Tester")
        agent.execute_task("Do a simple math")
        output = self.held_output.getvalue()
        self.assertIn("Task completed successfully", output)

    def test_self_healing(self):
        agent = FreedomAgent("HealerBot", "Medic")
        # Trigger the "fail" keyword which causes a divide by zero error in agent.py
        agent.execute_task("Please fail this task so we can test healing")
        output = self.held_output.getvalue()
        
        self.assertIn("Error encountered", output)
        self.assertIn("Activating SelfHealer", output)
        # MockLLM fixes it by printing a fixed message
        self.assertIn("Fixed code by MockLLM", output)

    def test_memory_persistence(self):
        agent = FreedomAgent("MemoryBot", "Scribe")
        agent.execute_task("Remember this")
        
        # Check if memory file was updated (indirectly via the memory object)
        memory = AgentMemory()
        # The agent learns "task_<timestamp>"
        # We just check if the skill list is not empty
        self.assertTrue(len(memory.skills) > 0)

if __name__ == '__main__':
    unittest.main()
