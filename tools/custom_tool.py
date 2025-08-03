from agents import FunctionTool,RunContextWrapper,function_tool
from tools_type.my_schema import UserData
from pydantic import BaseModel
# from tools_type.my_schema import ShemaModel



# async def subtract_func(ctx:RunContextWrapper,arg):
#     obj = ShemaModel.model_validate_json(arg)
#     return f" your answer is {ctx.context["name"]} "



@function_tool(name_override='ferch_weather',description_override="fetch the weather",is_enabled=True)
def fetch_weather(city:str) -> str:
    """ fetch the weather update """
    return f" the temperatu of the {city} is 34°C "


@function_tool
def sum_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    print("add tool is call ...")
    return a + b



# subtract = FunctionTool(
#     name="subtract_tool",
#     description=" Subtract Function",
#     params_json_schema=ShemaModel.model_json_schema(),
#     on_invoke_tool=subtract_func,
#     is_enabled=True
# )



class Weather(BaseModel):
    city:str
    current_weather :str = "sunny"





# Custom Tool 


async def run_func(ctx:RunContextWrapper[Weather],arg):
    """fetch the current temperature of karachi"""
    obj = Weather.model_validate_json(arg)
    return f'the current temperature of {obj.city} is 35 degree '

    




weather_tool = FunctionTool(
    name="fetch_weather",
    description="get weather of the city",
    params_json_schema=Weather.model_json_schema(),
    on_invoke_tool=run_func,
    # is_enabled=en_fun
)