# app.py

from flask import Flask, render_template, request, redirect, url_for # Added request, redirect, url_for for future steps
import json
import os

app = Flask(__name__)

# --- Configuration for Review File ---
REVIEW_FILE = "movie_reviews.json"
# ------------------------------------

# --- Helper Functions for Data Handling (reused from CLI app) ---
def load_reviews_from_file():
    """Loads movie reviews from a JSON file."""
    if os.path.exists(REVIEW_FILE):
        try:
            with open(REVIEW_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {REVIEW_FILE}. Returning empty list.")
            return []
        except IOError as e:
            print(f"Error loading reviews: {e}. Returning empty list.")
            return []
    return [] # Return empty list if file doesn't exist

def save_reviews_to_file(reviews_data):
    """Saves the given reviews data to a JSON file."""
    try:
        with open(REVIEW_FILE, 'w') as file:
            json.dump(reviews_data, file, indent=4)
        # print(f"Reviews saved to {REVIEW_FILE}") # Optional: for debugging
    except IOError as e:
        print(f"Error saving reviews: {e}")
# ---------------------------------------------------------------


# Define a route for the home page ('/')
@app.route('/')
def home():
    # Load reviews using our helper function
    current_reviews = load_reviews_from_file()
    # Pass the reviews list to the template
    return render_template('index.html', reviews=current_reviews)

# --- (Add New Review functionality will go here in the next phase) ---
# For now, we are just displaying


# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True)