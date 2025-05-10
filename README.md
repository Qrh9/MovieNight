# Movie Suggester

A simple Python script to search and filter movies from TMDb (The Movie Database) based on your favorite keywords and minimum rating.

---

## What It Does

* **Search**: Finds movies matching a text description (like "time loop dark truman show").
* **Filter**: Keeps only movies with a rating above a certain threshold (default is 3.6).
* **Notify**: If nothing matches, you get a friendly message saying no results.

---

## Requirements

* Python 3.x
* `requests` library (install with `pip install requests`)

---

## How to Use

1. Clone or download this repo.

2. Open the file and replace the placeholder `API_KEY` with your own TMDb API key.

3. Run the script from the terminal:

   ```bash
   python main.py
   ```

4. When prompted (or inside the code), change the search query to whatever you like:

   ```python
   search_movies("time loop")
   ```

---

## Customization

* **Minimum Rating**: Adjust `min_rating` in the function call to any value you prefer.
* **Language**: Change the `language` parameter (`en-US`) to another locale if you want.

---
