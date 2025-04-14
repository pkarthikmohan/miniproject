def calculate_median(data):
    data = sorted(data)
    n = len(data)
    
    if n % 2 == 1:
        return data[n // 2]
    else:
        mid1 = data[n // 2 - 1]
        mid2 = data[n // 2]
        return (mid1 + mid2) / 2
