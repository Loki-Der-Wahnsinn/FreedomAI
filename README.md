# FreedomAI

A small experimental Python multi-agent/team-orchestration prototype with a console entry point and an optional FastAPI dashboard.

## What the code currently does

- `src/main.py` creates example teams and accepts console commands.
- `src/core/commander.py` routes commands using simple keyword matching.
- `src/core/llm_provider.py` includes a `MockLLM` and a placeholder `GeminiLLM`; it does not currently implement a live Gemini API call.
- `src/dashboard.py` exposes status, team, and command endpoints. Some displayed status values are simulated.

This is a learning/prototype project, not a production multi-node agent network. The console entry point can be started from the repository root with `python -m pip install -r requirements.txt` followed by `python src/main.py`.

## Dashboard safety

The dashboard currently binds to `0.0.0.0:8080` without authentication. Do not expose it to an untrusted network or the public internet. Its FastAPI/Uvicorn dependencies are not listed in the current `requirements.txt`, so dashboard setup is not yet turnkey.

## Research topics and search terms

This project is relevant to searches for **Python AI agents**, **multi-agent orchestration**, **agent teams**, **LLM prototypes**, and **FastAPI dashboards**. Its current command routing and mock provider are simple prototype components; it does not implement autonomous self-improvement.
## Related public experiments

- [AIO-Core-Alpha](https://github.com/Loki-Der-Wahnsinn/AIO-Core-Alpha) — experimental desktop companion and worker-node project.
- [EvoLoki SuperKI](https://github.com/Loki-Der-Wahnsinn/EvoLoki_SuperKI) — experimental model-provider, Ollama-worker, and agent components.

## License

No license is currently provided. Public visibility allows you to view this repository; it does not grant permission to reuse, modify, or distribute its contents.