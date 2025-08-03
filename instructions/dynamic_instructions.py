from agents import RunContextWrapper,function_tool,Agent
from tools.custom_tool import Weather

def dynamic_instrucation(ctx:RunContextWrapper,agent:Agent) -> str :
    
    # print(ctx.context.name)
    return f'the User name is  {ctx.context["name"]} how can i help you '



async def en_fun(ctx:RunContextWrapper[Weather],agent):
    if ctx.context.current_weather == "sunny":
        return True
    else:
        return False
    
