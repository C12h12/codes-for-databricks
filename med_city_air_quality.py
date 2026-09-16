import numpy as np

def create_aqi_array(values:list)->np.ndarray:
    return np.array(values,dtype=np.int64)

def validate_aqi_array(arr:np.ndarray)->bool:
    if arr.size==0:
        return False
    return bool(np.all((arr>=0) & (arr<=100)))

def compute_aqi_stats(arr:np.ndarray)->tuple:
    avg=round(float(np.mean(arr)),2)
    std=round(float(np.std(arr)),2)
    max=round(float(np.max(arr)),2)
    min=round(float(np.min(arr)),2)

    return (avg,std,max,min)

def categorize_aqi(arr:np.ndarray)->np.ndarray:
    cat=[]
    for i in arr:
        if 0<=i<=50:
            cat.append('Good')
        elif 51<=i<=100:
            cat.append('Moderate')
        elif 101<=i<=150:
            cat.append('USG')
        elif 151 <=i<=200:
            cat.append('Unhealthy')
        elif 201 <= i<= 300:
            cat.append('Very Unhealthy')
        elif 301<= i <=500:
            cat.append('Hazardous')
    return np.array(cat)

def longest_unhealthy_streak(arr:np.ndarray)->int:
    max_streak=0
    current_streak=0

    for i in arr:
        if i>=151:
            current_streak+=1
            max_streak=max(max_streak,current_streak)
        else:
            current_streak=0
    return max_streak


# =========================================================
# TESTING
# =========================================================

print("===== AIR QUALITY AQI TESTING =====")

# Test 1: Create AQI Array
print("\n1. CREATE AQI ARRAY")
values = [32, 55, 85, 120, 165, 220, 325]

arr = create_aqi_array(values)

print("Input :", values)
print("Output:", arr)
print("Data Type:", arr.dtype)


# Test 2: Validate AQI Array
print("\n2. VALIDATE AQI ARRAY")

valid_arr = np.array([20, 50, 75, 100])
invalid_arr = np.array([20, -5, 75])
empty_arr = np.array([])

print("Valid data   :", validate_aqi_array(valid_arr))
print("Invalid data :", validate_aqi_array(invalid_arr))
print("Empty data   :", validate_aqi_array(empty_arr))


# Test 3: AQI Statistics
print("\n3. COMPUTE AQI STATISTICS")

stats_arr = np.array([52, 95, 172, 325])

print("Input :", stats_arr)
print("Output:", compute_aqi_stats(stats_arr))


# Test 4: Categorize AQI
print("\n4. CATEGORIZE AQI")

category_arr = np.array([32, 95, 120, 172, 250, 325])

print("Input :", category_arr)
print("Output:", categorize_aqi(category_arr))


# Test 5: Longest Unhealthy Streak
print("\n5. LONGEST UNHEALTHY STREAK")

streak_arr = np.array([130, 170, 180, 150, 165, 168])

print("Input :", streak_arr)
print("Output:", longest_unhealthy_streak(streak_arr))


