# a2a-multiple-agents-on-single-host

### Run agents on local:
```shell
cd a2a-multiple-agents-on-single-host
uv sync
export AGENT_URL=http://localhost:8000/a2a/
export GOOGLE_GENAI_USE_VERTEXAI=FALSE
export GOOGLE_API_KEY=********************
uv run main.py
```

### Test agents:
```shell
uv run a2a_client_app.py
```