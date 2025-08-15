import asyncio

from src.a2a.a2a_client import A2ASimpleClient


async def main():
    a2a_client: A2ASimpleClient = A2ASimpleClient()
    agent_host_url = "http://localhost:8000/a2a"
    trending_topics = await a2a_client.create_task(f'{agent_host_url}/trending', "What's trending today?")
    print(trending_topics)
    analysis = await a2a_client.create_task(f"{agent_host_url}/analyzer", "Analyze the trend AI in Social Media")
    print(analysis)


if __name__ == "__main__":
    asyncio.run(main())
