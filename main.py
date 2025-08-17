import logging
import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.a2a.a2a_utils import A2AUtils
from src.agent.analyzer_agent import get_analyzer_agent, get_analyzer_agent_card
from src.agent.conversation_agent import get_conversational_agent, get_conversational_agent_card
from src.agent.trending_topics_agent import get_trending_topics_agent, get_trending_topics_agent_card

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

AGENT_BASE_URL = os.getenv("AGENT_BASE_URL")

if not AGENT_BASE_URL:
    raise ValueError("AGENT_BASE_URL environment variable must be set")

MODEL_NAME = os.getenv("MODEL_NAME")

if not MODEL_NAME:
    raise ValueError("MODEL_NAME environment variable must be set")
logger.info(f"AGENT BASE URL {AGENT_BASE_URL}")

app: FastAPI = FastAPI(
    title="Run multiple agents on single host using A2A protocol.",
    description="Run multiple agents on single host using A2A protocol.",
    version="1.0.0",
    root_path="/a2a",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


# conversation agent integration with A2A server
A2AUtils.build(
    name="conversation",
    get_agent=get_conversational_agent,
    get_agent_card=get_conversational_agent_card,
    model_name=MODEL_NAME,
    agent_base_url=AGENT_BASE_URL,
    app=app,
)

# trending_topics agent integration with A2A server
A2AUtils.build(
    name="trending_topics",
    get_agent=get_trending_topics_agent,
    get_agent_card=get_trending_topics_agent_card,
    model_name=MODEL_NAME,
    agent_base_url=AGENT_BASE_URL,
    app=app,
)

# analyzer agent integration with A2A server
A2AUtils.build(
    name="analyzer",
    get_agent=get_analyzer_agent,
    get_agent_card=get_analyzer_agent_card,
    model_name=MODEL_NAME,
    agent_base_url=AGENT_BASE_URL,
    app=app,
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
