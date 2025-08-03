from agents import Agent ,ModelSettings
from agents.agent import StopAtTools
from instructions import dynamic_instructions
from my_config.gemini_config import Model
# from tools.custom_tool import subtract
from tools_type.my_schema import UserData
from tools.custom_tool import fetch_weather,sum_numbers,weather_tool
from my_agents.agent_2 import ai_agent

ai_tool = ai_agent.as_tool("ai_tool",tool_description="give answer about AI ")



assistant = Agent(
    name="assistant",
    instructions="you are ahelpful assistant giving answer as per the user prompt and calling relevent tool when user asked form you anything and you havent tool according to that question so simply say that sorry i am unable to answer this question call relevent tool accodance to user prompt  ",
    tools=[fetch_weather,sum_numbers,ai_tool],
    # tool_use_behavior=StopAtTools(stop_at_tool_names=["sum_numbers"])
    tool_use_behavior="run_llm_again"
)


