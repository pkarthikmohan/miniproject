from collections import Counter

def calculate_mode(numbers):
    counter = Counter(numbers)
    if not numbers:
        return None
    max_count = max(counter.values())
    modes = [num for num, count in counter.items() if count == max_count]
    if len(modes) == len(counter):
        return None  # No mode
    return modes
