# movie database
movies = [
    {"movie": "Piranha", "genre": "horror"},
    {"movie": "The bluff", "genre": "horror"},
    {"movie": "Kayara", "genre": "Animation"},
    {"movie": "wolf king", "genre": "Animation"},
    {"movie": "Seal Team", "genre": "action"},
    {"movie": "The outpost", "genre": "action"},
    {"movie": "The expanse", "genre": "Sci-fi"},
    {"movie": "World breaker", "genre": "Sci-fi"},
    {"movie": "Machine gunner", "genre": "romance"},
    {"movie": "blank", "genre": "romance"}
    {"movie": "conjuring", "genre": "horror"},
    {"movie": "rio", "genre": "Animation"},
    {"movie": "The little mermaid", "genre": "Animation"},
    {"movie": "cinderella", "genre": "Animation"},
]

# function to make recommendations
def recommend(movie_name):
    selected = None
    # find the movie
    for m in movies:
        if m["movie"].lower() == movie_name.lower():
            selected = m
            break

    # movie not found
    if not selected:
        print("Movie not found")
        return

    # get genre
    genre = selected["genre"]
    print(f"\n🎬 Recommendations (Genre: {genre}):\n")
    count = 0
    for m in movies:
        if m["genre"] == genre and m["movie"] != selected["movie"]:
            print(f"- {m['movie']}")
            count += 1
            if count == 3:
                break

# user input
name = input("Enter a movie name: ")
recommend(name)