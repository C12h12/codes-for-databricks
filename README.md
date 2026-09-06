



class GymWorkoutSystem:
    def __init__(self):
        self.data = {}

    def add_member(self, member_id, name, workout_type, workout_minutes):
        if member_id in self.data:
            raise ValueError("Member already exists")
        
        self.data[member_id] = {
            "name": name,
            "workout_type": workout_type,
            "workout_minutes": workout_minutes,
            "status": "Active"
        }
        
        return self.data

    def update_workout_minutes(self, member_id, new_minutes):
        if member_id not in self.data:
            raise KeyError("Member not found")
        
        self.data[member_id]["workout_minutes"] = new_minutes
        
        return self.data

    def get_member_details(self, member_id):
        if member_id not in self.data:
            raise KeyError("Member not found")
        
        return self.data[member_id]

    def get_active_members(self, minimum_minutes):
        return [
            mid for mid, info in self.data.items()
            if info["workout_minutes"] >= minimum_minutes
        ]
