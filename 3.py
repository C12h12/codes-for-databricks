import numpy as np

class EmployeePerformanceAnalyzer:

    def create_performance_array(self, scores_array: list) -> np.ndarray:
        return np.array(scores_array, dtype=int)

    def validate_scores(self, performance_array: np.ndarray) -> bool:
        if performance_array.size == 0:
            return False

        if np.any(performance_array < 0) or np.any(performance_array > 100):
            return False

        return True

    def compute_performance_summary(
        self,
        performance_array: np.ndarray
    ) -> tuple:
        performance_array = np.array(performance_array, dtype=float)

        total = np.sum(performance_array)
        average = round(np.mean(performance_array), 1)
        maximum = np.max(performance_array)

        return (total, average, maximum)

    def apply_bonus(self, performance_array: np.ndarray) -> np.ndarray:
        result = performance_array.astype(float)

        mask = result > 85
        result[mask] = result[mask] * 1.05

        result = np.clip(result, 0, 100)
        return np.round(result, 1)

    def categorize_employees(
        self,
        performance_array: np.ndarray
    ) -> np.ndarray:
        result = []

        for score in performance_array:
            if score >= 90:
                result.append("Excellent")
            elif score >= 80:
                result.append("Good")
            else:
                result.append("Needs Improvement")

        return np.array(result)

    def format_scores_with_grades(
        self,
        performance_array: np.ndarray
    ) -> np.ndarray:
        result = []

        for score in performance_array:
            if score >= 90:
                result.append("A")
            elif score >= 80:
                result.append("B")
            elif score >= 70:
                result.append("C")
            else:
                result.append("D")

        return np.array(result)