import os
import requests

def fetch_recipes(query, diet="", intolerances="", maxCarbs="", minProtein="", maxFat="", maxReadyTime=""):
    apiKey = os.getenv("API_KEY")
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": apiKey,
        "query": query,
        "number": 5,
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
