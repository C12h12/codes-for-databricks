import numpy as np


def create_temperature_array(values: list) -> np.ndarray:
    return np.array(values, dtype=np.float64)


def validate_temperature_array(arr: np.ndarray) -> bool:
    if arr.size == 0:
        return False

    if not np.issubdtype(arr.dtype, np.number):
        return False

    return bool(np.all((arr >= -30.0) & (arr <= 10.0)))


def compute_temperature_stats(arr: np.ndarray) -> tuple:
    mean = round(float(np.mean(arr)), 2)
    standard_deviation = round(float(np.std(arr)), 2)
    maximum = round(float(np.max(arr)), 2)
    minimum = round(float(np.min(arr)), 2)

    return (mean, standard_deviation, maximum, minimum)


def categorize_temperatures(arr: np.ndarray) -> np.ndarray:
    categories = []

    for value in arr:
        if -30.0 <= value <= -18.0:
            categories.append("Frozen")
        elif -18.0 < value <= 5.0:
            categories.append("Chilled")
        elif 5.0 < value <= 10.0:
            categories.append("Warning")
        else:
            categories.append("Invalid")

    return np.array(categories)


def longest_warning_streak(arr: np.ndarray) -> int:
    longest = 0
    current = 0

    for value in arr:
        if 5.0 < value <= 10.0:
            current += 1
            longest = max(longest, current)
        else:
            current = 0

    return longest