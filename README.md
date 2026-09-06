

class EmployeeSalaryAnalyzer:
    
    def __init__(self):
        self.salary_data = {}

    def parse_records(self, records):
        for record in records.strip().split("\n"):
            name, salary = record.split(",")
            self.salary_data[name] = float(salary)
        return self.salary_data

    def total_salary(self):
        total = 0.0
        for salary in self.salary_data.values():
            total += salary
        return total

    def apply_raise(self, percentage):
        for name in self.salary_data:
            self.salary_data[name] += self.salary_data[name] * percentage / 100
        return self.salary_data

    def top_earners(self, n):
        sorted_data = sorted(
            self.salary_data.items(),
            key=lambda item: item[1],
            reverse=True
        )
        return dict(sorted_data[:n])
