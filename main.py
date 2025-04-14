import difflib
import re
from median import calculate_median
from add import calculate_add
from divide import calculate_division
from equations import extract_equation, solve_equation
from sympy import rem, symbols, Eq, solve
from google_search import google_search_summary

def calculate_mean(numbers):
    if not numbers:
        return "No numbers provided."
    return sum(numbers) / len(numbers)

def calculate_mode(numbers):
    if not numbers:
        return "No numbers provided."
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_freq]
    if len(modes) == 1:
        return modes[0]
    return modes  # Can be multiple modes

def parse_numbers(text):
    try:
        return [float(word) for word in text.split() if word.replace('.', '', 1).isdigit()]
    except ValueError:
        return []

print("Hey! I'm your mini AI. You can ask me to find the 'mean', 'mode', or even ask me to 'define' something!")

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["exit", "quit"]:
        print("AI: Goodbye!")
        break

    words = user_input.split()

    # Check for "define" anywhere
    if any(difflib.get_close_matches(word, ["define", "search","what is","wts","?","wt"], n=1, cutoff=0.8) for word in words):
        query = user_input.replace("define", "").strip()
        if query:
            print(f"AI: Searching for '{query}'...")
            result = google_search_summary(query)
            print(f"AI: {result}")
        else:
            print("AI: What do you want me to define?")
        continue

    # Check for "mean" anywhere
    if any(difflib.get_close_matches(word, ["mean"], n=1, cutoff=0.9) for word in words):
        numbers = parse_numbers(user_input)
        if numbers:
            result = calculate_mean(numbers)
            print(f"AI: Mean is {result}")
        else:
            print("AI: Please give me some numbers, like 'mean of 2 4 6'")
        continue

    # check for addd or sum like words any where
    if any(difflib.get_close_matches(word, ["add","sum"], n=1, cutoff=0.9) for word in words):
        numbers = parse_numbers(user_input)
        if numbers:
            result = calculate_add(numbers)
            print(f"AI: Sum is {result}")
        else:
            print("AI: Please give me some numbers, like 'mean of 2 4 6'")
        continue

    #check for Divide...
    if any(difflib.get_close_matches(word, ["divide","div","/"], n=1, cutoff=0.9) for word in words):
        numbers = parse_numbers(user_input)
        if numbers:
            result = calculate_division(numbers)
            print(f"AI: Answer is {result}")
        else:
            print("AI: Please give me some numbers, like 'calculate mean or add 2 4 6'")
        continue

    # Check for "mode" anywhere
    if any(difflib.get_close_matches(word, ["mode"], n=1, cutoff=0.8) for word in words):
        numbers = parse_numbers(user_input)
        if numbers:
            result = calculate_mode(numbers)
            print(f"AI: Mode is {result}")
        else:
            print("AI: Please give me some numbers, like 'mode of 2 4 6'")
        continue

    



# Get user input

    if any(difflib.get_close_matches(word, [" equation","evaluate"], n=1, cutoff=0.8) for word in words):
# Try to extract the equation
        equation = extract_equation(user_input)
        
        if equation:
            try:
                print(equation)
                print("🧠 Processing:", equation)
                result = solve_equation(equation)
                print(result)
            except Exception as e:
                print("❌ Error:", e)
        else:
            print("❌ Couldn't understand your input.")
        
        
    
    #check for median...
    if any(difflib.get_close_matches(word, ["median"], n=1, cutoff=0.8) for word in words):
        numbers = parse_numbers(user_input)
        if numbers:
            result = calculate_median(numbers)
            print(f"AI: Median is {result}")
        else:
            print("AI: Please give me some numbers, like 'mean, mode or median of 2 4 6'")
        continue
    # Nothing matched
    print("AI: I can help with math or definitions. Try something like 'define gravity' or 'mean of 2 4 6'.")
