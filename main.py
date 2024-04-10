import os
from dotenv import load_dotenv
from entity import create_thread, start, get_response

load_dotenv()

def get_recipe_query():
    user_query_prompt = "Please provide a recipe query: "
    return input(user_query_prompt)


def get_user_preferences():
    diet = input("Enter your dietary preference (e.g., vegetarian, vegan, etc.): ")
    intolerances = input("Enter any intolerances (e.g., dairy, gluten, etc.): ")
    maxCarbs = input("Enter the maximum carbs allowed (in grams): ")
    minProtein = input("Enter the minimum protein required (in grams): ")
    maxFat = input("Enter the maximum fat allowed (in grams): ")
    maxReadyTime = input("Enter the maximum ready time (in minutes): ")
    return diet, intolerances, maxCarbs, minProtein, maxFat, maxReadyTime


def handle_recipe_assistance(thread_id, assistant_id):
    user_query = get_recipe_query()
    diet, intolerances, maxCarbs, minProtein, maxFat, maxReadyTime = get_user_preferences()
    start(thread_id, user_query)
    response = get_response(thread_id, assistant_id, user_query, diet, intolerances, maxCarbs, minProtein, maxFat, maxReadyTime)
    print("Recipes:", response)
    return response

def handle_further_assistance(thread_id, assistant_id, response):
    while True:
        further_assistance = input("Do you require further assistance? (yes/no): ")
        if further_assistance.lower() == 'no':
            print("Thanks for using our service. Goodbye!")
            return
            # This line breaks out of the function, effectively stopping the program
        elif further_assistance.lower() == 'yes':
                response = handle_recipe_assistance(thread_id, assistant_id)
                continue
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def main():
    thread_id = create_thread()

    while True:
        user_query = get_recipe_query()
        diet, intolerances, maxCarbs, minProtein, maxFat, maxReadyTime = get_user_preferences()

        assistant_id = os.getenv("ASSISTANT_ID")
        
        start(thread_id, user_query)

        response = get_response(thread_id, assistant_id, user_query, diet, intolerances, maxCarbs, minProtein, maxFat, maxReadyTime)
        print("Recipes:", response)

        handle_further_assistance(thread_id, assistant_id, response)
        break
if __name__ == "__main__":
    main()
