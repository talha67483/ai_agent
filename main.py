from agents import Runner,RunConfig
from my_agents.agent_1 import assistant
from my_config.gemini_config import Model,client
from tools.custom_tool import Weather
from my_agents.agent_2 import ai_agent


config = RunConfig(model=Model,model_provider=client,tracing_disabled=True)



prompt = input("Enter your Question ")
result = Runner.run_sync(starting_agent=ai_agent,input=prompt,run_config=config)

print(result.final_output)


