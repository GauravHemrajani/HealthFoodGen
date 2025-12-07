from flask import Flask, render_template, request, session
import google.generativeai as genai
from dotenv import load_dotenv
import os, json

load_dotenv()
app = Flask(__name__)
app.secret_key = "supersecretkey"

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

 
@app.route("/")
def index():
    return render_template("index.html")


data = None
@app.route("/output", methods=["POST", "GET"])
def process():
    global data 
    ing = request.form.get("ingredients", "").strip()
    mealType = request.form.get("type", "").strip()

    prompt = model.generate_content(f"""You are a Healthy Meal Generator AI.

Your task is to generate exactly 5 healthy meals that use ONLY the ingredients provided by the user, and all ingredients must be included in each recipe. You may add water, salt, pepper, or common spices if absolutely necessary, but avoid adding any other ingredients.

USER INPUT:
Ingredients: {ing}
Meal type: {mealType}

REQUIREMENTS:
- Generate exactly 5 meals.
- Each meal must use ONLY the provided ingredients.
- Each meal must match the requested meal type (breakfast, lunch, dinner, snack, etc).
- You must create original recipes — do NOT search the web and do NOT provide external links.
- For each meal, include:
    1. name
    2. calories (kcal) (approximate)
    3. protein (g)
    4. fats (g)
    5. carbs (g)
    6. cooking_time (minutes)
    7. ingredients_with_quantities
    8. step_by_step_instructions
    9. the recipe page with MEAL_INDEX being from 0,1,2,3,4
- Return ONLY valid JSON formatted as follows:"""+"""

{
  "meals": [
    {
      "name": "",
      "calories": 0kcal,
      "protein": 0g,
      "fat": 0g,
      "carbs": 0g,
      "prep_time": "",
      "ingredients": [
        { "item": "", "quantity": "" }
      ],
      "instructions": [
        "step 1...",
        "step 2..."
      ],
      "recipe_page": "/recipe/MEAL_INDEX"
    }
  ]
}"""+f"""

3. Ingredient rules (IMPORTANT):
   - Use ONLY the ingredients provided by the user: "{ing}"
   - ALL ingredients provided by the user must appear in each recipe.
   - DO NOT add any ingredients that are not in the user's list, except for basic items like salt, pepper, water, or oil.
   - The meal type MUST match "{mealType}".
   - The quantity should also have the unit with it

4. Nutrition requirements:
   - calories, protein, fat, and carbs must be realistic estimates and it should be with its units.

5. Prep details:
   - "prep_time" should be a readable string (e.g., "12 minutes").

7. Output EXACTLY 5 meals.

8. Output must be strictly valid JSON and fully parsable.

Now generate the meals.

""")

    output = prompt.text[7:-3]
    data = json.loads(output)
    session["meals"] = data  # meals_json is the dict returned by AI
    print(data)
    
    return render_template("output.html", data=data)

@app.route('/recipe/<int:meal_id>')
def recipe_page(meal_id):
    meals = session.get("meals", {})
    meal = meals["meals"][meal_id]
    return render_template("recipe.html", meal=meal)


if __name__ == "__main__":
    app.run(debug=True, port=5100)