from typing import Callable

from a2a.types import AgentCard
from fastapi import FastAPI
from google.adk.agents import LlmAgent

from src.a2a.a2a_fastapi_app import A2AFastApiApp
from src.a2a.a2a_request_handler import A2ARequestHandler


class A2AUtils:
    """
    Utility class for A2A (Agent-to-Agent) communication.

    This class provides static methods to assist in constructing and managing agent
    communication processes in the A2A framework. It is specifically designed to help
    configure and set up agents, their request handlers, and their associated API endpoints.

    """
    @staticmethod
    def build(
            name: str,
            get_agent: Callable[[str], LlmAgent],
            get_agent_card: Callable[[str], AgentCard],
            model_name: str,
            agent_base_url: str,
            app: FastAPI,
    ) -> None:
        agent = get_agent(model_name)
        agent_request_handler = A2ARequestHandler.get_request_handler(agent)
        agent_card = get_agent_card(f"{agent_base_url}/{name}/")
        agent_server = A2AFastApiApp(fastapi_app=app, agent_card=agent_card, http_handler=agent_request_handler)
        agent_server.build(rpc_url=f"/{name}/", agent_card_url=f"/{name}/{{path:path}}")

