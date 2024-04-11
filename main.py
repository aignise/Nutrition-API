import os
from dotenv import load_dotenv
from entity import create_thread, start, get_response
import json

load_dotenv()

assistant_id = os.getenv("ASSISTANT_ID")
thread_id = create_thread()


def main():
    
    print("Hey! Welcome, Please type in your query below,enter quit to exit the conversation!")
    
    diet = input("Enter your dietary preference (e.g., vegetarian, vegan, etc.): ")
    intolerances = input("Enter any intolerances (e.g., dairy, gluten, etc.): ")
    maxCarbs = input("Enter the maximum carbs allowed (in grams): ")
    minProtein = input("Enter the minimum protein required (in grams): ")
    maxFat = input("Enter the maximum fat allowed (in grams): ")
    maxReadyTime = input("Enter the maximum ready time (in minutes): ")
    while True:
        prompt = input("User:  ")
        if prompt.lower() == "quit":
            break

        start(thread_id, prompt)
        response = get_response(thread_id, assistant_id, prompt, diet, intolerances, maxCarbs, minProtein, maxFat, maxReadyTime)
        print("Agent: ", response)


if __name__ == "__main__":
    main()

