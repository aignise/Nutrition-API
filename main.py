from flask import Flask, request, render_template
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

def get_api_key():
    return os.getenv("API_KEY")

def get_recipe_information(recipe_id, apiKey):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {
        "apiKey": apiKey,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_recipes(query, apiKey, diet, intolerances, maxCarbs, maxCalories, minProtein,maxAlcohol, maxFat , maxReadyTime):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": apiKey,
        "query": query,
        "number": 5,  # Adjust the number of results as needed
        "diet": diet,
        "intolerances": intolerances,
        "maxCarbs": maxCarbs,
        "maxCalories": maxCalories,
        "minProtein": minProtein,
        "maxFat":maxFat,
        "maxAlcohol":maxAlcohol,
        "maxReadyTime":maxReadyTime,
        "includeRecipeInformation":True,
        "addRecipeNutrition":True,
        "includeNutrition": True,
        "instructionsRequired": "true"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def index():
    return 'Welcome to Recipe Search!'

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        apiKey = get_api_key()  # Retrieve API key from environment variable
        query = request.form['query']
        diet = request.form['diet']
        intolerances = request.form['intolerances']
        maxCarbs = request.form['maxCarbs']
        maxCalories = request.form['maxCalories']  
        minProtein = request.form['minProtein']
        maxAlcohol = request.form['maxAlcohol']
        maxFat = request.form['maxFat']
        maxReadyTime = request.form['maxReadyTime']
        recipes = get_recipes(query, apiKey, diet, intolerances, maxCarbs, maxCalories, minProtein,maxAlcohol, maxFat , maxReadyTime)
        print(recipes)
        if recipes and 'results' in recipes:
            return render_template('results.html', recipes=recipes['results'])
        else:
            return "No recipes found or there was an error in the request."
    else:
        return "Send a POST request to this endpoint with query parameters."

if __name__ == "__main__":
    app.run(debug=True)
