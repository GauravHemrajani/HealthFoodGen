# 🥗 HealthFoodGen – AI Meal Generator Flask Web App

HealthFoodGen is an AI-powered recipe generator that suggests 5 custom meals based on your selected ingredients and meal type.
Each meal links to a dedicated recipe page created entirely by the AI — no external websites required.

This project uses Flask, TailwindCSS, Google Gemini API, and Jinja2 to create a clean, modern, dark-mode web experience.

## 🚀 Features

✓ Enter ingredients + meal type  
✓ AI generates 5 meal suggestions  
✓ Each suggestion links to its own recipe page  
✓ Recipes include steps, ingredient quantities, and instructions  
✓ TailwindCSS dark-mode UI  
✓ Stateful navigation (return to suggestions without regenerating)  
✓ Zero external recipe links — AI creates everything internally  
✓ Clean routing using Flask sessions  

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, Jinja2, TailwindCSS
- **AI Model:** Google Gemini
- **Runtime:** Python 3.x
- **Session Storage:** Flask session (dictionary-based)

## 📁 Project Structure

```
/
├── static/
│   └── your CSS, tailwind, assets...
├── templates/
│   ├── index.html       # Input form page
│   ├── output.html      # AI's 5-meal suggestion page
│   └── recipe.html      # Individual recipe page
├── app.py               # Flask backend logic
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 📦 Requirements

Include these in `requirements.txt`:

```
Flask
google-generativeai
python-dotenv
```

Optional (if used):

```
jinja2
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the root folder:

```env
GOOGLE_API_KEY=your_api_key_here
FLASK_SECRET_KEY=your_random_secret_key
```

## ▶️ How to Run

1. **Clone the repo:**

```bash
git clone <your_repo_link>
cd <project_folder>
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the Flask server:**

```bash
python app.py
```

4. **Open your browser and go to:**

```
http://127.0.0.1:5000
```

## 🧠 How HealthFoodGen Works (Step-by-Step)

### 1️⃣ User inputs ingredients & meal type

Example: chicken, tomato, garlic  
Meal type: Lunch

### 2️⃣ Flask sends this data to the AI

The master prompt ensures the AI only uses the given ingredients.

### 3️⃣ AI returns 5 structured meal objects

Each meal includes:
- title
- calories
- protein, fats, carbs
- ingredients list with quantities
- step-by-step instructions

Flask stores this in:

```python
session["meals"] = meals
```

### 4️⃣ Output page shows the 5 meals

Each item links to:

```
/recipe/<id>
```

### 5️⃣ Recipe page displays the full recipe

Since the recipe is already stored in the session, clicking "Back" does not regenerate new meals.

## 🔗 Navigation

- `/` → input page
- `/output` → list of 5 generated meals
- `/recipe/<meal_id>` → single meal recipe

## 🎨 Styling

- TailwindCSS used for all styling
- Modern dark mode theme
- Desktop-focused layout
- Clean UI using utility classes only

## 🧪 Example Data Flow

```
User Input → POST /output → AI Generates Meals → Stored in session → User clicks meal → GET /recipe/<id>
```

## 🤝 Contributing

Pull requests are welcome!  
Please ensure your changes follow the existing code structure.
