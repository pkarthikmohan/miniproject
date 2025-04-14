import difflib
from duck_search import duckduckgo_search

print("Hey! I'm your math bot. You can ask me to find the 'mean', 'mode', or even ask me to 'define' something!")

while True:
    user_input = input("You: ").strip().lower()
    
    # Suggest correction if it's a close match to 'define'
    words = user_input.split()
    if words:
        corrected = difflib.get_close_matches(words[0], ["define"], n=1, cutoff=0.8)
        if corrected and corrected[0] == "define":
            query = " ".join(words[1:]).strip()
            if query:
                print(f"Bot: Searching for '{query}'...")
                result = duckduckgo_search(query)
                print(f"Bot: {result}")
                continue

    # Handle exit
    if user_input == "exit":
        print("Bot: See ya!")
        break

    print("Bot: I can help with math or definitions. Try something like 'define gravity' or 'mean of 2 4 6'.")
