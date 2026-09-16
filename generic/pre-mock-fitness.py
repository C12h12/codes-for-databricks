class FitnessTracker:
    def __init__(self):
        pass
    def register_user(self,fitness_data:dict,user_name:str)->dict:
        fitness_data[user_name]={
            'workouts':0,
            'calories':0,
            'status':'Inactive'
        }

        return fitness_data

    def log_workout(self,fitness_data:dict,user_name:str,calories_burned:int)->dict:
        if user_name not in fitness_data:
            raise KeyError('Error: User not found')
        fitness_data[user_name]['workouts']+=1
        fitness_data[user_name]['calories']+=calories_burned

        if fitness_data[user_name]['workouts']>5:
            fitness_data[user_name]['status']='Active'

        return fitness_data

    def calculate_average_calories(self,fitness_data:dict,user_name:str)->float:
        if fitness_data[user_name]['workouts']==0:
            raise KeyError('Error: Invalid user or no workouts')
        average=fitness_data[user_name]['calories']/fitness_data[user_name]['workouts']
        return float(average)

    def generate_progress_report(self,fitness_data:dict)->dict:
        report={}
        for k,v in fitness_data.items():
            if v['calories'] < 1000:
                report[k]='Beginner'
            elif 1000<= v['calories'] < 5000:
                report[k]='Intermediate'
            else:
                report[k]='Advanced'
        return report

# ==============================
# TESTING FITNESS TRACKER
# ==============================

tracker = FitnessTracker()

print("\n===== TEST CASE 1: REGISTER USER =====")
fitness_data = {}

result = tracker.register_user(fitness_data, "Alice")
print(result)


print("\n===== TEST CASE 2: LOG WORKOUT =====")
result = tracker.log_workout(fitness_data, "Alice", 300)
print(result)


print("\n===== TEST CASE 3: LOG MULTIPLE WORKOUTS =====")
tracker.log_workout(fitness_data, "Alice", 400)
tracker.log_workout(fitness_data, "Alice", 500)
tracker.log_workout(fitness_data, "Alice", 600)
tracker.log_workout(fitness_data, "Alice", 700)
tracker.log_workout(fitness_data, "Alice", 800)

print(fitness_data)


print("\n===== TEST CASE 4: CALCULATE AVERAGE CALORIES =====")
average = tracker.calculate_average_calories(fitness_data, "Alice")
print("Average calories:", round(average, 2))


print("\n===== TEST CASE 5: GENERATE PROGRESS REPORT =====")
report = tracker.generate_progress_report(fitness_data)
print(report)


print("\n===== TEST CASE 6: REGISTER ANOTHER USER =====")
tracker.register_user(fitness_data, "Bob")
tracker.log_workout(fitness_data, "Bob", 1200)

print(fitness_data)


print("\n===== TEST CASE 7: TEST INVALID USER =====")
try:
    tracker.log_workout(fitness_data, "Charlie", 300)
except KeyError as e:
    print("Caught expected error:", e)


print("\n===== TEST CASE 8: TEST AVERAGE WITH NO WORKOUTS =====")

tracker.register_user(fitness_data, "Charlie")

try:
    tracker.calculate_average_calories(fitness_data, "Charlie")
except KeyError as e:
    print("Caught expected error:", e)