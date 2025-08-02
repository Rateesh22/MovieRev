# app.py

# This list will hold all our movie review dictionaries.
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

def view_reviews():
    """Displays all existing movie reviews."""
    print("\n--- All Movie Reviews ---")
    if not movie_reviews: # Checks if the list is empty
        print("No reviews added yet. Add some movies first!")
        return # Exit the function if no reviews

    for i, review in enumerate(movie_reviews):
        # i is the index (0, 1, 2...), review is the dictionary itself
        print(f"--- Review #{i + 1} ---") # +1 to make it human-readable (start from 1)
        print(f"Title: {review['title']}")
        # We can represent stars visually
        stars = "⭐" * review['rating'] + "☆" * (5 - review['rating']) # Example: ⭐⭐⭐☆☆
        print(f"Rating: {review['rating']}/5 {stars}")
        print(f"Review: {review['review']}")
        print("--------------------") # Separator for readability

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
            add_review()
        elif choice == '2':
            view_reviews() # Call the new view_reviews function
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break # Exit the while loop
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# This ensures main() runs only when the script is executed directly
if __name__ == "__main__":
    main()