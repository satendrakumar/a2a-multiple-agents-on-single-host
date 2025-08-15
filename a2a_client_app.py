import asyncio

from src.a2a.a2a_client import A2ASimpleClient


async def main():
    a2a_client: A2ASimpleClient = A2ASimpleClient()
    agent_host_url = "http://localhost:8000/a2a"
    
    trending_task = a2a_client.create_task(f'{agent_host_url}/trending', "What's trending today?")
    analysis_task = a2a_client.create_task(f"{agent_host_url}/analyzer", "Analyze the trend AI in Social Media")

    trending_topics, analysis = await asyncio.gather(trending_task, analysis_task)
    print(trending_topics)
    print(analysis)


if __name__ == "__main__":
    asyncio.run(main())
