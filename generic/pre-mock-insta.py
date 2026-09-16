import numpy as np

def create_views_array(views_data:list)->np.ndarray:
    return np.array(views_data,dtype=np.int64)

def validate_views_array(views_array:np.ndarray)->bool:
    if views_array.size==0:
        return False
    if not np.issubdtype(views_array.dtype,np.number):
        return False
    return bool(np.all(views_array >= 0))

def compute_view_metrics(views_array:np.ndarray)->tuple:
    total=int(np.sum(views_array))
    maximum=int(np.max(views_array))
    average=round(float(np.mean(views_array)),2)

    return (total,average,maximum)

def categorize_trend_levels(views_array:np.ndarray)->np.ndarray:
    category=[]
    for i in views_array:
        if i < 3000:
            category.append('Low Trend')
        elif 3000 <= i <= 4999:
            category.append('Moderate Trend')
        else:
            category.append('Viral Trend')
    return np.array(category)

def longest_growth_streak(views_array:np.ndarray)->int:
    current_streak=1
    max_streak=1

    n=len(views_array)

    if n==1:
        return 1
    if n==0:
        return 0

    for i in range(1,n):
        if views_array[i] > views_array[i-1]:
            current_streak+=1
        else:
            current_streak=1
        max_streak=max(max_streak,current_streak)
    return max_streak

def format_views_counts(views_array:np.ndarray)->np.ndarray:
    return np.array([f'{int(i):,}' for i in views_array])



# ==============================
# TESTING INSTAGRAM REEL ANALYSIS
# ==============================

print("\n===== TEST CASE 1: CREATE VIEWS ARRAY =====")

views_data = [1200, 3600, 1900, 5400, 7800]

views_array = create_views_array(views_data)

print("Views array:", views_array)
print("Data type:", views_array.dtype)


print("\n===== TEST CASE 2: VALIDATE VIEWS ARRAY =====")

print("Valid array:", validate_views_array(views_array))

invalid_array = np.array([1500, 3600, -2800, 5500])

print("Invalid array:", validate_views_array(invalid_array))


print("\n===== TEST CASE 3: COMPUTE VIEW METRICS =====")

metrics = compute_view_metrics(views_array)

print("Total, Average, Maximum:", metrics)


print("\n===== TEST CASE 4: CATEGORIZE TREND LEVELS =====")

trend_levels = categorize_trend_levels(views_array)

print("Trend levels:", trend_levels)


print("\n===== TEST CASE 5: LONGEST GROWTH STREAK =====")

growth_data = np.array([1500, 1200, 2800, 2900, 3200, 1200, 5600])

streak = longest_growth_streak(growth_data)

print("Longest growth streak:", streak)


print("\n===== TEST CASE 6: FORMAT VIEW COUNTS =====")

format_data = np.array([5200, 55000, 3700000])

formatted_views = format_views_counts(format_data)

print("Formatted views:", formatted_views)