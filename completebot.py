import requests
import json

# Define the base URL for the Spoonacular API
BASE_URL = "https://api.spoonacular.com"

# Define the API key
API_KEY = "e1b8c32c48e04995873639eabcec965f"

# Define the available endpoints
ENDPOINTS = {
    "Recipe Information": "/recipes/{recipe_id}/information?includeNutrition=true",
    "Recipe Search": "/recipes/complexSearch",
    "Random Recipes": "/recipes/random",
    "Food and Grocery": "/food/products/search",
    "Meal Planning": "/mealplanner/generate",
    "Wine Pairing": "/food/wine/pairing",
    "Menu Items": "/food/menuItems/search",
    "Talk to Chatbot": "/food/converse"
}

# Define a function to handle each endpoint
def recipe_information():
    recipe_id = input("Enter the recipe ID: ")
    url = f"{BASE_URL}{ENDPOINTS['Recipe Information']}".format(recipe_id=recipe_id)
    params = {"apiKey": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        recipe = response.json()
        print("Recipe Name:", recipe["title"])
        print("Ingredients:")
        for ingredient in recipe["extendedIngredients"]:
            print("-", ingredient["name"])
        print("Instructions:")
        print(recipe["instructions"])
    else:
        print("Error:", response.status_code)

def talk_to_chatbot():
    text = input("Enter your question/request for the chatbot: ")
    context_id = input("Enter the context id (optional): ")
    url = f"{BASE_URL}{ENDPOINTS['Talk to Chatbot']}"
    params = {
        "apiKey": API_KEY,
        "text": text,
        "contextId": context_id,
        "number":10
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        chatbot_response = response.json()
        print("Chatbot Response:")
        print(chatbot_response["answerText"])
        print()
    else:
        print(f"Error: {response.status_code}")
        
def recipe_search(query, apiKey, diet, intolerances, maxCarbs, minProtein):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": apiKey,
        "query": query,
        "number": 5,  # Adjust the number of results as needed
        "diet": diet,
        "intolerances": intolerances,
        "maxCarbs": maxCarbs,
        "minProtein": minProtein,
        "instructionsRequired": "true"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def random_recipes():
    url = f"{BASE_URL}{ENDPOINTS['Random Recipes']}"
    params = {"apiKey": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        recipes = response.json()
        for recipe in recipes["recipes"]:
            print("Recipe Name:", recipe["title"])
            print("Ingredients:")
            for ingredient in recipe["extendedIngredients"]:
                print("-", ingredient["name"])
            print("Instructions:")
            print(recipe["instructions"])
            print()
    else:
        print("Error:", response.status_code)

def food_and_grocery():
    query = input("Enter the food or grocery item: ")
    url = f"{BASE_URL}{ENDPOINTS['Food and Grocery']}"
    params = {"apiKey": API_KEY, "query": query}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        items = response.json()
        print(items)
        for item in items["products"]:
            print("Product Name:", item["title"])
            print("Product ID:", item["id"])
            print("Image URL:", item["image"])
            print()
    else:
        print("Error:", response.status_code)

def meal_planning():
    url = f"{BASE_URL}{ENDPOINTS['Meal Planning']}"
    params = {"apiKey": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        meal_plan = response.json()
        print("Meal Plan:")
        for day, meals in meal_plan["week"].items():
            print(day)
            for meal in meals:
                print("  -", meal["title"])
        print()
    else:
        print("Error:", response.status_code)

def wine_pairing():
    food = input("Enter the food item: ")
    url = f"{BASE_URL}{ENDPOINTS['Wine Pairing']}"
    params = {"apiKey": API_KEY, "food": food}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        pairings = response.json()
        print("Wine Pairings:")
        print(pairings["pairingText"])

def menu_items():
    url = f"{BASE_URL}{ENDPOINTS['Menu Items']}"
    params = {"apiKey": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        menu_items = response.json()
        print(menu_items)
        for item in menu_items["menuItems"]:
            print("Item Name:", item["title"])
            print("Description:", item["description"])
            print("Price:", item["price"])
            print()
    else:
        print("Error:", response.status_code)

# Define a function to explain each endpoint
def explain_endpoints():
    print("Here is what each endpoint does:")
    for i, endpoint in enumerate(ENDPOINTS.keys(), start=1):
        print(f"{i}. {endpoint}")
        if endpoint == "Recipe Information":
            print("   Get detailed information about a specific recipe.")
        elif endpoint == "Recipe Search":
            print("   Search for recipes based on various criteria.")
        elif endpoint == "Random Recipes":
            print("   Get a random selection of recipes based on various criteria.")
        elif endpoint == "Food and Grocery":
            print("   Get information about food and grocery items.")
        elif endpoint == "Meal Planning":
            print("   Create meal plans based on various criteria.")
        elif endpoint == "Wine Pairing":
            print("   Get information about wine pairing.")
        elif endpoint == "Menu Items":
            print("   Get information about menu items from various restaurants.")
        elif endpoint == "Talk to Chatbot":
            print("   Create custom recipes based on specific criteria.")
        print()

# Define a function to ask the user which endpoint they want to use
def ask_user():
    print("Which endpoint would you like to use?")
    for i, endpoint in enumerate(ENDPOINTS.keys(), start=1):
        print(f"{i}. {endpoint}")
    choice = int(input("Enter the number of the endpoint you want to use: "))
    return choice

# Define a function to handle the user's choice
def handle_choice(choice):
    if choice == 1:
        recipe_information()
    elif choice == 2:
        recipe_search()
    elif choice == 3:
        random_recipes()
    elif choice == 4:
        food_and_grocery()
    elif choice == 5:
        meal_planning()
    elif choice == 6:
        wine_pairing()
    elif choice == 7:
        menu_items()
    elif choice == 8:
        talk_to_chatbot()  # Add this line to handle the new option
    else:
        print("Invalid choice")

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
# Main function
def main():
    query = input("Enter a recipe name to search for: ")
    diet = input("Enter your diet (e.g., vegetarian, vegan, etc.): ")
    intolerances = input("Enter your intolerances (e.g., gluten, dairy, etc.): ")
    maxCarbs = input("Enter the maximum carbs you want in the recipe: ")
    minProtein = input("Enter the minimum protein you want in the recipe: ")
    
    recipes = recipe_search(query, API_KEY, diet, intolerances, maxCarbs, minProtein)
    if recipes and 'results' in recipes:
        for recipe in recipes['results']:
            print(f"Recipe ID: {recipe['id']}, Title: {recipe['title']}")
            recipe_info = get_recipe_information(recipe['id'], API_KEY)
            if recipe_info and 'instructions' in recipe_info:
                print(f"Instructions: {recipe_info['instructions']}")
            else:
                print("Instructions not available for this recipe.")
            if 'nutrition' in recipe:
                for nutrient in recipe['nutrition']['nutrients']:
                    if nutrient['name'] == 'Protein':
                        print(f"Protein: {nutrient['amount']} {nutrient['unit']}")
                    elif nutrient['name'] == 'Carbohydrates':
                        print(f"Carbs: {nutrient['amount']} {nutrient['unit']}")
    else:
        print("No recipes found or there was an error in the request.")
    print()
    print()
    print("What do you want to do next?")
    explain_endpoints()
    choice = ask_user()
    handle_choice(choice)

# Run the main function
if __name__ == "__main__":
    main()
