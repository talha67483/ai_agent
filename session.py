from agents import Runner,SQLiteSession 
import asyncio
from my_config.gemini_config import Model,client
from agents import Agent,Runner,RunConfig

simple_agent = Agent(
    name="General Purpose Agent",
    instructions="You are helful agent",
)

config = RunConfig(model=Model,model_provider=client,tracing_disabled=True)

async def main():
  prompt = input("Enter your question: ")
  result = await Runner.run(starting_agent=simple_agent,input=prompt,run_config=config)
  print(result.final_output)

  prompt = input(f"\n\nEnter your question: ")
  new_prompt = result.to_input_list() + [{"role":"user","content":prompt}] # providing the context to the llm
  result = await Runner.run(starting_agent=simple_agent,input=new_prompt,run_config=config)
  print(result.final_output)


#-----------------------------------------------------------------------------------------------
async def main_new():  
  my_session = SQLiteSession('session_id_123',"my_conversation.db") # built in class for session by open ai agent sdk
  prompt = input("Enter your question: ")
  result = await Runner.run(starting_agent=simple_agent,input=prompt,run_config=config,session=my_session)
  print(result.final_output)

  prompt = input("Enter your question: ")
   # providing the context to the llm
  result = await Runner.run(starting_agent=simple_agent,input=prompt,run_config=config,session=my_session)
  print(result.final_output)

asyncio.run(main_new())

