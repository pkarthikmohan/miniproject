from serpapi import GoogleSearch

def google_search_summary(query):
    """
    Searches Google via SerpApi and returns the top result's snippet.
    """
    params = {
        "engine": "google",
        "q": query,
        "api_key": ""
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results.get("organic_results", [])

        if organic_results:
            return organic_results[0].get("snippet", "No summary found.")
        else:
            return "No results found."

    except Exception as e:
        return f"Something went wrong: {e}"
