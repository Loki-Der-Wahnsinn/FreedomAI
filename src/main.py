import sys
import time
from core.commander import Commander

def main():
    print("Initializing FreedomAI v1.0...")
    commander = Commander()

    # Create Teams
    commander.create_team("Red Team", ["Agent-Alpha", "Agent-Beta", "Agent-Gamma"])
    commander.create_team("Blue Team", ["Agent-Delta", "Agent-Epsilon", "Agent-Zeta"])

    print("\nFreedomAI is online and awaiting orders.")
    print("Type 'exit' to quit.")

    while True:
        try:
            command = input("\n[USER] >> ")
            if command.lower() in ["exit", "quit"]:
                print("Shutting down FreedomAI.")
                break
            
            if not command.strip():
                continue

            commander.issue_command(command)
            time.sleep(1) # Pause for effect

        except KeyboardInterrupt:
            print("\nForce shutdown initiated.")
            break
        except Exception as e:
            print(f"System Error: {e}")

if __name__ == "__main__":
    main()
