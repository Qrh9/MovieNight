import requests
API_KEY = "your api key" #from https://api.themoviedb.org

def search_movies(query, min_rating=3.6):
    """
    Search for movies using the TMDB API.
    Args:
        query (str): The search query (movie title).
        min_rating (float): Minimum rating to filter movies.
    Returns:
        None
    
    """
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": API_KEY,
        "query": query,
        "language": "en-US",
        "page": 1
    }
    resp = requests.get(url, params=params)
    data = resp.json()

    films = [
        m for m in data.get("results", [])
        if m.get("vote_average", 0) > min_rating
    ]

    if not films:
        print(f"No movies found for '{query}' with rating above {min_rating}.")
    if resp.status_code != 200:
        print(f"Error: {resp.status_code} - {resp.text}")
    if not API_KEY:
        print("API key is missing. Please provide a valid API key.")
    if not films:
        print("No movies found.")
    if not API_KEY:
        return

    for movie in films:
        print(f"\n🎬 {movie['title']}")
        print(f"🌍 Language: {movie.get('original_language', 'N/A')}")
        print(f"📅 Release Date: {movie.get('release_date', 'N/A')}")
        print(f"⭐ Rating: {movie.get('vote_average', 'N/A')}")
        print(f"📝 Overview: {movie.get('overview', 'No description')}")
        print("-" * 50)

if __name__ == "__main__":
    search_movies("time loop")
