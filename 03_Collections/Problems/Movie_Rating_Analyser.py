"""
# Problem 08 : Movie Rating Analyzer

Analyze movie ratings and generate a report based on audience
ratings.

Requirements : 
1. Calculate the average rating of each movie.
2. Find the highest-rated movie.
3. Find the lowest-rated movie.
4. Display movies with a rating of 4.0 or above.
5. Sort movies by rating.
"""

ratings = {
    "Inception": [5, 4, 5, 4, 5],
    "Interstellar": [5, 5, 4, 5, 4],
    "The Dark Knight": [5, 5, 5, 4, 5],
    "Avatar": [4, 3, 4, 4, 3],
    "Titanic": [4, 4, 5, 4, 5]
}

average_ratings = {
    movie: sum(scores) / len(scores)
    for movie, scores in ratings.items()
}

highest_rated = max(average_ratings, key=average_ratings.get)
lowest_rated = min(average_ratings, key=average_ratings.get)

popular_movies = {
    movie: rating
    for movie, rating in average_ratings.items()
    if rating >= 4.0
}

sorted_movies = sorted(
    average_ratings.items(),
    key=lambda item: item[1],
    reverse=True
)

print("===== MOVIE RATING REPORT =====")

print("\nAverage Ratings:")
for movie, rating in sorted_movies:
    print(f"{movie:<20}: {rating:.2f}")

print(f"\nHighest Rated: {highest_rated} ({average_ratings[highest_rated]:.2f})")
print(f"Lowest Rated : {lowest_rated} ({average_ratings[lowest_rated]:.2f})")

print("\nMovies Rated 4.0 or Above:")
for movie in popular_movies:
    print(f"{movie}: {popular_movies[movie]:.2f}")


# Output:
# ===== MOVIE RATING REPORT =====
#
# Average Ratings:
# The Dark Knight    : 4.80
# Inception           : 4.60
# Interstellar        : 4.60
# Titanic             : 4.40
# Avatar              : 3.60
#
# Highest Rated: The Dark Knight (4.80)
# Lowest Rated : Avatar (3.60)
#
# Movies Rated 4.0 or Above:
# Inception: 4.60
# Interstellar: 4.60
# The Dark Knight: 4.80
# Titanic: 4.40