from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from google.adk import Runner
from google.adk.a2a.executor.a2a_agent_executor import A2aAgentExecutor, A2aAgentExecutorConfig
from google.adk.agents import LlmAgent
from google.adk.artifacts import InMemoryArtifactService
from google.adk.memory import InMemoryMemoryService
from google.adk.sessions import InMemorySessionService


class A2ARequestHandler:
    @staticmethod
    def get_request_handler(agent: LlmAgent):
        runner = Runner(
            app_name=agent.name,
            agent=agent,
            artifact_service=InMemoryArtifactService(),
            session_service=InMemorySessionService(),
            memory_service=InMemoryMemoryService(),
        )
        config = A2aAgentExecutorConfig()
        executor = A2aAgentExecutor(runner=runner, config=config)
        return DefaultRequestHandler(agent_executor=executor, task_store=InMemoryTaskStore())
