from flask import Flask, request, jsonify
import os
import openai
import requests
from dotenv import load_dotenv
import time

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai_api_key)

app = Flask(__name__)

def fetch_recipes(query, diet="", intolerances="", maxCarbs="", minProtein="", maxFat="", maxReadyTime=""):
    apiKey = os.getenv("API_KEY")
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": apiKey,
        "query": query,
        "number": 5,  # Adjust the number of results as needed
        "diet": diet,
        "intolerances": intolerances,
        "maxCarbs": maxCarbs,
        "minProtein": minProtein,
        "maxFat": maxFat,
        "maxReadyTime": maxReadyTime,
        "includeRecipeInformation": True,
        "addRecipeNutrition": True,
        "includeNutrition": True,
        "instructionsRequired": "true"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/fetch-recipes', methods=['POST'])
def get_recipes():
    data = request.json
    user_query = data.get('query')
    diet = data.get('diet', "")
    intolerances = data.get('intolerances', "")
    maxCarbs = data.get('maxCarbs', "")
    minProtein = data.get('minProtein', "")
    maxFat = data.get('maxFat', "")
    maxReadyTime = data.get('maxReadyTime', "")

    response = fetch_recipes(user_query, diet, intolerances, maxCarbs, minProtein, maxFat, maxReadyTime)

    output_str = ""
    if response and 'results' in response:
        for index, recipe in enumerate(response['results'], start=1):
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

    return jsonify({"response": output_str})

if __name__ == "__main__":
    app.run(debug=True)
