# a2a-multiple-agents-on-single-host

This repository demonstrates how to run **multiple A2A agents** on the **same host** using the A2A protocol.
Each agent is served at a **unique URL path**, making it possible to host different agents without requiring multiple servers or ports.

---

## 📌 Example Setup

Two agents running on the same host:

| Agent Name | URL |
|------------|-----|
| Trending   | [http://localhost:8000/a2a/trending/.well-known/agent-card.json](http://localhost:8000/a2a/trending/.well-known/agent-card.json) |
| Analyzer   | [http://localhost:8000/a2a/analyzer/.well-known/agent-card.json](http://localhost:8000/a2a/analyzer/.well-known/agent-card.json) |


---

## 🚀 Running Agents Locally

1.  Clone the repository
    ```bash
    git clone https://github.com/satendrakumar/a2a-multiple-agents-on-single-host.git
    cd a2a-multiple-agents-on-single-host
    ```

2.  Install dependencies (using uv)
    ```bash
    uv sync
    ```

3.  Set environment variables
    *   Copy `.env-sample` to `.env`
        ```bash
        cp .env-sample .env
        ```
    *   Update values as needed

4.  Start the agents
    ```bash
    uv run main.py
    ```

---

## 🧪 Testing the Agents:

Run the provided client app to send test requests:

```shell
uv run a2a_client_app.py
```

---

## 📂 Project Structure

```text
a2a-multiple-agents-on-single-host/
├── README.md
├── a2a_client_app.py
├── main.py
├── pyproject.toml
├── src
│ ├── __init__.py
│ ├── a2a
│ │ ├── __init__.py
│ │ ├── a2a_client.py
│ │ └── a2a_fastapi_app.py
│ └── agent
│     ├── __init__.py
│     ├── analyzer_agent.py
│     └── trending_topics_agent.py
└── uv.lock

```

---

## ✅ Requirements

Key dependencies defined in `pyproject.toml`:

*   `a2a-sdk`
*   `google-adk`

---

## Notes

- This setup demonstrates hosting multiple agents via unique URL paths behind a single application server.
- If you run behind a reverse proxy, ensure the `/a2a/...` paths are forwarded to the app.
- For local development, keep your working directory at the project root so relative imports and paths resolve correctly.