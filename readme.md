# Nutrition Focused - Recipe Search App

The Recipe Search App is a Flask-based web application that allows users to search for recipes based on various criteria such as dietary preferences, ingredients, and nutritional information. It utilizes the Spoonacular API to fetch recipe data and provide users with relevant recipes.

# Fetch Recipes Function

This Python function `fetch_recipes` utilizes the Spoonacular API to fetch recipes based on various parameters such as query, dietary preferences, and nutritional requirements.

## Parameters

- `query`: The search query for recipes.
- `diet`: Dietary preference for the recipes (e.g., vegetarian, vegan, etc.). Defaults to an empty string.
- `intolerances`: Intolerances for the recipes (e.g., dairy, gluten, etc.). Defaults to an empty string.
- `maxCarbs`: Maximum allowed carbs in grams. Defaults to an empty string.
- `minProtein`: Minimum required protein in grams. Defaults to an empty string.
- `maxFat`: Maximum allowed fat in grams. Defaults to an empty string.
- `maxReadyTime`: Maximum ready time for the recipes in minutes. Defaults to an empty string.

## Returns

The function returns a JSON response containing the fetched recipes.

# Main Program

This Python script `main.py` interacts with the user to fetch recipes based on their preferences using the `fetch_recipes` function.

## Steps to Run

1. Set up a virtual environment and install the required dependencies (`dotenv`, `requests`).
2. Obtain an API key from Spoonacular and set it in the `.env` file.
3. Execute the `main.py` script.
4. Enter the recipe query and other preferences as prompted.
5. The script will fetch and display the recipes based on the provided preferences.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- pip

# Setting Up OpenAI Assistant Using OpenAI API

Follow these steps to set up your OpenAI assistant using the OpenAI API:

1. **Sign Up for OpenAI API**:
   - Visit the OpenAI website and sign up for an account if you haven't already.
   - Subscribe to the OpenAI API plan that suits your needs.

2. **Get API Key**:
   - Once subscribed, you'll receive an API key. This key is essential for authenticating your requests.

3. **Install OpenAI Python Library**:
   - Use pip to install the OpenAI Python library:
     ```
     pip install openai
     ```

4. **Import OpenAI Library**:
   - In your Python script or environment, import the OpenAI library:
     ```python
     import openai
     ```

5. **Set API Key**:
   - Set your API key using the `openai.api_key` attribute:
     ```python
     openai.api_key = 'YOUR_API_KEY'
     ```

6. **Invoke OpenAI API**:
   - Use the OpenAI API to interact with the language model. For example:
     ```python
     response = openai.Completion.create(
         engine="text-davinci-003",
         prompt="Once upon a time",
         max_tokens=50
     )
     print(response.choices[0].text.strip())
     ```

7. **Explore API Documentation**:
   - Refer to the official OpenAI API documentation for detailed information on endpoints, parameters, and usage examples.

8. **Understand API Usage and Billing**:
   - Familiarize yourself with usage limits and billing details to avoid exceeding quotas and unexpected charges.

9. **Experiment and Develop**:
   - Start experimenting with the OpenAI models, explore prompts, and develop your applications.

10. **Handle Errors and Exceptions**:
    - Implement error handling mechanisms in your code to gracefully handle any errors during API requests.

By following these steps, you can set up and start using the OpenAI API to interact with powerful language models and build innovative applications leveraging artificial intelligence capabilities.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/recipe-search-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd recipe-search-app
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Open a web browser and go to `http://localhost:5000` to access the Recipe Search App.

3. Enter your search query, dietary preferences, and other criteria to find recipes that match your criteria.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- The Recipe Search App utilizes the Spoonacular API to fetch recipe data.
- Special thanks to the contributors who helped improve this project.
