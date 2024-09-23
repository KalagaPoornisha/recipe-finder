import requests

def get_recipes(ingredients):
    api_key = 'eea3c2163fb4449b86fe79615ff874d8'  # Your API key
    url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return the recipe data
    else:
        print("Error fetching recipes")
        return None

if __name__ == "__main__":
    user_input = input("Enter ingredients (comma separated): ")
    recipes = get_recipes(user_input)
    if recipes:
        for recipe in recipes:
            print(recipe['title'])  # Print the recipe titles
 
