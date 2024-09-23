import tkinter as tk
from tkinter import messagebox
import requests

def get_recipes():
    ingredients = entry.get()
    api_key = 'eea3c2163fb4449b86fe79615ff874d8'  # Your API key
    url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        recipes = response.json()
        output.delete(1.0, tk.END)  # Clear previous results
        if recipes:
            for recipe in recipes:
                output.insert(tk.END, recipe['title'] + '\n')
        else:
            output.insert(tk.END, "No recipes found.")
    else:
        messagebox.showerror("Error", "Failed to fetch recipes.")

# Create the main window
root = tk.Tk()
root.title("Recipe Finder")

# Create input field
tk.Label(root, text="Enter ingredients (comma separated):").pack()
entry = tk.Entry(root, width=50)
entry.pack()

# Create a button to fetch recipes
button = tk.Button(root, text="Find Recipes", command=get_recipes)
button.pack()

# Create a text box to display results
output = tk.Text(root, height=15, width=50)
output.pack()

# Start the GUI loop
root.mainloop()
 
