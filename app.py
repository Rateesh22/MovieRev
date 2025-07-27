# app.py

# Task 2: Data Storage Structure
# This list will hold all our movie review dictionaries.
# It's declared globally so all functions can access it.
movie_reviews = []

def add_review():
    """Prompts the user for movie details and adds a new review."""
    print("\n--- Add New Movie Review ---")
    title = input("Enter movie title: ")

    # Input validation for rating
    while True:
        try:
            rating_str = input("Enter rating (1-5 stars): ")
            rating = int(rating_str)
            if 1 <= rating <= 5:
                break # Valid rating, exit loop
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number for the rating.")

    review_text = input("Enter your review (briefly): ")

    # Create a dictionary for the new review
    new_review = {
        "title": title,
        "rating": rating,
        "review": review_text
    }

    # Add the new review dictionary to our list
    movie_reviews.append(new_review)
    print(f"'{title}' review added successfully!")

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Movie Reviewer Menu ---")
    print("1. Add a New Movie Review")
    print("2. View All Movie Reviews")
    print("3. Exit")
    print("---------------------------")

def main():
    """Main function to run the Movie Reviewer application."""
    print("Welcome to your CLI Movie Reviewer!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_review() # Call the new add_review function
        elif choice == '2':
            print("You chose to view reviews.")
            # We will call the view_reviews() function here later
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break # Exit the while loop
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# This ensures main() runs only when the script is executed directly
if __name__ == "__main__":
    main()