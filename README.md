# multiple-agents-on-single-a2a-server

This repository demonstrates how to run **multiple A2A agents** on the **same host** using the A2A protocol.
Each agent is served at a **unique URL path**, making it possible to host different agents without requiring multiple servers or ports.

---

## 📌 Example Setup

Three agents running on the same host:

| Agent Name            | Agent card URL                                                                                                    |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| Conversational Agent  | [http://localhost:8000/a2a/conversation/agent-card.json](http://localhost:8000/a2a/conversation/agent-card.json) |
| Trending topics Agent | [http://localhost:8000/a2a/trending/agent-card.json](http://localhost:8000/a2a/trending/agent-card.json) |
| Analyzer Agent        | [http://localhost:8000/a2a/analyzer/agent-card.json](http://localhost:8000/a2a/analyzer/agent-card.json) |


---

## 🚀 Running Agents Locally

1.  Clone the repository
    ```bash
    git clone https://github.com/satendrakumar/multiple-agents-on-single-a2a-server.git
    cd multiple-agents-on-single-a2a-server
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

## 🧪 Testing Agents using A2AClient:

  Run the provided client app to send test requests:

  ```bash
    uv run a2a_client_app.py
  ```

## Testing Agents Using CURL request:
   ```bash
   Request:
   curl --location 'http://localhost:8000/a2a/conversation/' \
        --header 'Content-Type: application/json' \
        --header 'Accept: text/event-stream' \
        --data '{
            "id": "6a39c736-fff7-45f8-b2b0-c44e705d2474",
            "jsonrpc": "2.0",
            "method": "message/stream",
            "params": {
                "configuration": {
                    "acceptedOutputModes": [],
                    "blocking": "True"
                },
                "message": {
                    "contextId": "8bffff7b-3abc-4d85-bcce-0bcdbe321017",
                    "kind": "message",
                    "messageId": "82642fd2-f270-4a56-a7d9-5d26fddabc95",
                    "parts": [
                        {
                            "kind": "text",
                            "text": "Who is PM of India?"
                        }
                    ],
                    "role": "user"
                }
            }
        }'
    Reponse:
    {
        "id": "6a39c736-fff7-45f8-b2b0-c44e705d2474",
        "jsonrpc": "2.0",
        "result": {
            "artifact": {
                "artifactId": "9474e1ac-1e35-425c-9c18-238b07739e6d",
                "parts": [
                    {
                        "kind": "text",
                        "text": "As of today, August 16, 2025, the Prime Minister of India is **Narendra Modi**.\n\nHe has been serving as the Prime Minister since May 26, 2014, and was sworn in for his third consecutive term on June 9, 2024, following the 2024 Parliamentary elections."
                    }
                ]
            },
            "contextId": "8bffff7b-3abc-4d85-bcce-0bcdbe321017",
            "kind": "artifact-update",
            "lastChunk": true,
            "taskId": "23a93002-686b-4c8a-8bb6-ec649acea0c3"
        }
    }    
   ```

---

## How to run inside Docker:
```bash
# Docker build
docker build -t multiple-agents-on-single-a2a-server:v1.0.0 .
# Docker run
docker run --env-file ./.env -e PORT=8000 -p 8000:8000  multiple-agents-on-single-a2a-server:v1.0.0
```


---

## Notes

- This setup demonstrates hosting multiple agents via unique URL paths behind a single application server.
- If you run behind a reverse proxy, ensure the `/a2a/...` paths are forwarded to the app.
- For local development, keep your working directory at the project root so relative imports and paths resolve correctly.