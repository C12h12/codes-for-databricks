import numpy as np


def create_views_array(views_data: list) -> np.ndarray:
    return np.array(views_data, dtype=np.int64)


def validate_views_array(views_array: np.ndarray) -> bool:
    if views_array.size == 0:
        return False

    if not np.issubdtype(views_array.dtype, np.number):
        return False

    return bool(np.all(views_array >= 0))


def compute_view_metrics(views_array: np.ndarray) -> tuple:
    total_views = int(np.sum(views_array))
    average_views = round(float(np.mean(views_array)), 2)
    maximum_views = int(np.max(views_array))

    return total_views, average_views, maximum_views


def categorize_trend_levels(views_array: np.ndarray) -> np.ndarray:
    return np.select(
        [
            views_array < 3000,
            (views_array >= 3000) & (views_array < 5000),
            views_array >= 5000
        ],
        [
            "Low Trend",
            "Moderate Trend",
            "Viral Trend"
        ]
    )


def longest_growth_streak(views_array: np.ndarray) -> int:
    n = len(views_array)

    if n == 0:
        return 0

    if n == 1:
        return 1

    current_streak = 1
    longest_streak = 1

    for i in range(1, n):
        if views_array[i] > views_array[i - 1]:
            current_streak += 1
        else:
            current_streak = 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak


def format_view_counts(views_array: np.ndarray) -> np.ndarray:
    return np.array([f"{int(value):,}" for value in views_array])