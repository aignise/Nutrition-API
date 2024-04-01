import time
import openai
import os
from function import fetch_recipes
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai_api_key)

def setup():
    assistant = client.beta.assistants.create(
        name="Recipe Search Assistant",
        instructions="You are a bot to search for recipes based on user input.",
        model="gpt-4-turbo-preview",
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "fetch_recipes",
                    "description": "Fetches recipes from Spoonacular API based on user input.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Recipe query to search"
                            },
                            "diet": {
                                "type": "string",
                                "description": "Dietary preference (optional)"
                            },
                            "intolerances": {
                                "type": "string",
                                "description": "Intolerances (optional)"
                            },
                            "maxCarbs": {
                                "type": "string",
                                "description": "Maximum carbs allowed (optional)"
                            },
                            "minProtein": {
                                "type": "string",
                                "description": "Minimum protein required (optional)"
                            },
                            "maxFat": {
                                "type": "string",
                                "description": "Maximum fat allowed (optional)"
                            },
                            "maxReadyTime": {
                                "type": "string",
                                "description": "Maximum ready time in minutes (optional)"
                            }
                        },
                        "required": ["query"]
                    }
                }
            }
        ]
    )

    return assistant.id

def create_thread():
    thread = client.beta.threads.create()
    return thread.id

def start(thread_id, user_query):
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_query
    )
    
def get_response(thread_id, assistant_id, user_query, diet, intolerances, maxCarbs, minProtein, maxFat, maxReadyTime):
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions="Answer user questions using custom functions available to you."
    )
    
    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        if run_status.status == "completed":
            break
        elif run_status.status == 'requires_action':
            submit_tool_outputs(thread_id, run.id, run_status, user_query, diet, intolerances, maxCarbs, minProtein, maxFat, maxReadyTime)
        
        time.sleep(1)
    
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    response = messages.data[0].content[0].text.value
    return response

def submit_tool_outputs(thread_id, run_id, run_status, user_query, diet, intolerances, maxCarbs, minProtein, maxFat, maxReadyTime):
    output = fetch_recipes(query=user_query, diet=diet, intolerances=intolerances, maxCarbs=maxCarbs, minProtein=minProtein, maxFat=maxFat, maxReadyTime=maxReadyTime)
    output_str = ""
    if output and 'results' in output:
        for index, recipe in enumerate(output['results'], start=1):
            output_str += f"Recipe {index}: {recipe['title']}\n"
            output_str += f"  Ready in {recipe['readyInMinutes']} minutes\n"
            output_str += f"  Link: {recipe['sourceUrl']}\n"
            output_str += f"  Servings: {recipe['servings']}\n"
            output_str += "  Nutritional Information:\n"
            for nutrient in recipe['nutrition']['nutrients']:
                output_str += f"    - {nutrient['name']}: {nutrient['amount']} {nutrient['unit']} ({nutrient['percentOfDailyNeeds']}% of daily needs)\n"
            output_str += "\n"
    else:
        output_str = "No recipes found."

    tool_calls = run_status.required_action.submit_tool_outputs.tool_calls
    
    tool_outputs = []
    for tool_call in tool_calls:
        tool_outputs.append({
            "tool_call_id": tool_call.id,
            "output": output_str
        })
    
    client.beta.threads.runs.submit_tool_outputs(
        thread_id=thread_id,
        run_id=run_id,
        tool_outputs=tool_outputs
    )

def main():
    thread_id = create_thread()

    user_query_prompt = "Please provide a recipe query: "
    user_query = input(user_query_prompt)

    diet = input("Enter your dietary preference (e.g., vegetarian, vegan, etc.): ")
    intolerances = input("Enter any intolerances (e.g., dairy, gluten, etc.): ")
    maxCarbs = input("Enter the maximum carbs allowed (in grams): ")
    minProtein = input("Enter the minimum protein required (in grams): ")
    maxFat = input("Enter the maximum fat allowed (in grams): ")
    maxReadyTime = input("Enter the maximum ready time (in minutes): ")

    assistant_id = os.getenv("ASSISTANT_ID")
    
    start(thread_id, user_query)

    response = get_response(thread_id, assistant_id, user_query, diet, intolerances, maxCarbs, minProtein, maxFat, maxReadyTime)

    print("Recipes:", response)

if __name__ == "__main__":
    main()
