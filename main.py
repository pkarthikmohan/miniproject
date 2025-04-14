from flask import Flask, request, jsonify
import difflib
from median import calculate_median
from add import calculate_add
from divide import calculate_division
from equations import extract_equation, solve_equation
from google_search import google_search_summary
from sympy import symbols, Eq, solve

app = Flask(__name__)

# Helper function to parse numbers from input
def parse_numbers(text):
    try:
        return [float(word) for word in text.split() if word.replace('.', '', 1).isdigit()]
    except ValueError:
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_input():
    user_input = request.json['prompt'].strip().lower()
    words = user_input.split()

    # Define different AI actions based on user input

    # Google Search
    if any(difflib.get_close_matches(word, ["define", "search", "what is"], n=1, cutoff=0.8) for word in words):
        query = user_input.replace("define", "").strip()
        result = google_search_summary(query)
        return jsonify({"response": result})

    # Mean Calculation
    if any(difflib.get_close_matches(word, ["mean"], n=1, cutoff=0.9) for word in words):
        numbers = parse_numbers(user_input)
        if numbers:
            result = sum(numbers) / len(numbers)
            return jsonify({"response": f"The mean is {result}"})
        return jsonify({"response": "Please provide numbers for the mean calculation."})

    # Mode Calculation
    if any(difflib.get_close_matches(word, ["mode"], n=1, cutoff=0.8) for word in words):
        numbers = parse_numbers(user_input)
        if numbers:
            result = calculate_mode(numbers)  # Your existing function for mode
            return jsonify({"response": f"The mode is {result}"})
        return jsonify({"response": "Please provide numbers for mode calculation."})

    # Median Calculation
    if any(difflib.get_close_matches(word, ["median"], n=1, cutoff=0.8) for word in words):
        numbers = parse_numbers(user_input)
        if numbers:
            result = calculate_median(numbers)
            return jsonify({"response": f"The median is {result}"})
        return jsonify({"response": "Please provide numbers for median calculation."})

    # Equation Solving
    if any(difflib.get_close_matches(word, ["equation"], n=1, cutoff=0.8) for word in words):
        equation = extract_equation(user_input)
        if equation:
            try:
                result = solve_equation(equation)  # Your existing equation solver
                return jsonify({"response": f"The solution is {result}"})
            except Exception as e:
                return jsonify({"response": f"Error solving equation: {e}"})
        return jsonify({"response": "Could not extract the equation. Please provide a valid equation."})

    # Addition Calculation
    if any(difflib.get_close_matches(word, ["add", "sum"], n=1, cutoff=0.9) for word in words):
        numbers = parse_numbers(user_input)
        if numbers:
            result = calculate_add(numbers)  # Your existing function for addition
            return jsonify({"response": f"The sum is {result}"})
        return jsonify({"response": "Please provide numbers to add."})

    return jsonify({"response": "Sorry, I didn't understand that. Try something like 'mean of 1 2 3' or 'define gravity'."})

if __name__ == '__main__':
    app.run(debug=True)
