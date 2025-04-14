from flask import Flask, request, render_template, jsonify
import difflib
from median import calculate_median
from add import calculate_add
from divide import calculate_division
from equations import extract_equation, solve_equation
from google_search import google_search_summary

app = Flask(__name__)

def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else "No numbers provided."

def calculate_mode(numbers):
    freq = {num: numbers.count(num) for num in numbers}
    max_freq = max(freq.values())
    return [num for num, f in freq.items() if f == max_freq]

def parse_numbers(text):
    return [float(word) for word in text.split() if word.replace('.', '', 1).isdigit()]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message'].strip().lower()
    words = user_input.split()

    if any(difflib.get_close_matches(word, ["define", "search", "what is"], n=1, cutoff=0.8) for word in words):
        query = user_input.replace("define", "").strip()
        return jsonify({"response": google_search_summary(query)})

    elif any(difflib.get_close_matches(word, ["mean"], n=1, cutoff=0.9) for word in words):
        numbers = parse_numbers(user_input)
        return jsonify({"response": f"Mean is {calculate_mean(numbers)}"})

    elif any(difflib.get_close_matches(word, ["add", "sum"], n=1, cutoff=0.9) for word in words):
        numbers = parse_numbers(user_input)
        return jsonify({"response": f"Sum is {calculate_add(numbers)}"})

    elif any(difflib.get_close_matches(word, ["divide", "div", "/"], n=1, cutoff=0.9) for word in words):
        numbers = parse_numbers(user_input)
        return jsonify({"response": f"Answer is {calculate_division(numbers)}"})

    elif any(difflib.get_close_matches(word, ["mode"], n=1, cutoff=0.8) for word in words):
        numbers = parse_numbers(user_input)
        return jsonify({"response": f"Mode is {calculate_mode(numbers)}"})

    elif any(difflib.get_close_matches(word, ["equation", "evaluate"], n=1, cutoff=0.8) for word in words):
        equation = extract_equation(user_input)
        if equation:
            return jsonify({"response": str(solve_equation(equation))})
        return jsonify({"response": "❌ Couldn't understand your equation."})

    elif any(difflib.get_close_matches(word, ["median"], n=1, cutoff=0.8) for word in words):
        numbers = parse_numbers(user_input)
        return jsonify({"response": f"Median is {calculate_median(numbers)}"})

    return jsonify({"response": "I can help with math or definitions. Try 'mean of 2 4 6' or 'define gravity'."})

if __name__ == '__main__':
    app.run(debug=True)
