

class ClinicQueueSystem:


    def __init__(self):
        self.queue_data = {}

    def add_department(self, department: str, waiting_count: int) -> dict:
        self.queue_data[department] = waiting_count
        return self.queue_data

    def update_waiting_count(self, department: str, new_count: int) -> dict:
        if department not in self.queue_data:
            raise KeyError("Department not found")

        self.queue_data[department] = new_count
        return self.queue_data

    def crowded_departments(self, threshold: int) -> dict:
        result = {}

        for department, count in self.queue_data.items():
            if count > threshold:
                result[department] = count

        return result

    def assign_queue_actions(self) -> dict:
        actions = {}

        for department, count in self.queue_data.items():
            if count > 60:
                actions[department] = "Open Extra Counter"
            elif count >= 25:
                actions[department] = "Normal Queue"
            else:
                actions[department] = "Fast Queue"

        return actions
