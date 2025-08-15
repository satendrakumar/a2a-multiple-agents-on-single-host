# a2a-multiple-agents-on-single-host

### Run agents on local:

```shell
git clone https://github.com/satendrakumar/a2a-multiple-agents-on-single-host.git
cd a2a-multiple-agents-on-single-host
uv sync
# rename .env-sample into .env and update the env params
uv run main.py
```

### Test agents:

```shell
uv run a2a_client_app.py
```