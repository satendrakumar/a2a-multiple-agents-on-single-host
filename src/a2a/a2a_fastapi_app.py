from collections.abc import Callable
from typing import Any

from a2a.server.apps.jsonrpc.jsonrpc_app import CallContextBuilder, JSONRPCApplication
from a2a.server.context import ServerCallContext
from a2a.server.request_handlers.request_handler import RequestHandler
from a2a.types import AgentCard
from a2a.utils.constants import AGENT_CARD_WELL_KNOWN_PATH, DEFAULT_RPC_URL, EXTENDED_AGENT_CARD_PATH
from fastapi import APIRouter, FastAPI
from starlette.applications import Starlette


class A2AFastApiApp(JSONRPCApplication):
    def __init__(
            self,
            fastapi_app: FastAPI,
            agent_card: AgentCard,
            http_handler: RequestHandler,
            extended_agent_card: AgentCard | None = None,
            context_builder: CallContextBuilder | None = None,
            card_modifier: Callable[[AgentCard], AgentCard] | None = None,
            extended_card_modifier: Callable[[AgentCard, ServerCallContext], AgentCard] | None = None,
    ):
        super().__init__(
            agent_card=agent_card,
            http_handler=http_handler,
            extended_agent_card=extended_agent_card,
            context_builder=context_builder,
            card_modifier=card_modifier,
            extended_card_modifier=extended_card_modifier,
        )
        self.fastapi_app = fastapi_app

    def build(
            self,
            agent_card_url: str = AGENT_CARD_WELL_KNOWN_PATH,
            rpc_url: str = DEFAULT_RPC_URL,
            extended_agent_card_url: str = EXTENDED_AGENT_CARD_PATH,
            **kwargs: Any,
    ) -> Starlette:
        name_prefix = rpc_url.replace("/", "")
        router = APIRouter()
        router.add_api_route(
            rpc_url,
            endpoint=self._handle_requests,
            name=f"{name_prefix}_a2a_handler",
            methods=["POST"],
        )
        router.add_api_route(
            agent_card_url,
            endpoint=self._handle_get_agent_card,
            methods=["GET"],
            name=f"{name_prefix}_agent_card",
        )
        self.fastapi_app.include_router(router)
        return self.fastapi_app
