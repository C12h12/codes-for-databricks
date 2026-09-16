#numpy question #cold storage
import numpy as np

def create_temperature_array(values:list)->np.ndarray:
    arr=np.array(values,dtype=np.float64)
    return arr

def validate_temperature_array(arr:np.ndarray)->bool:
    if arr.size==0:
        return False
    if not np.issubdtype(arr.dtype,np.number):
        return False
    return bool(np.all((arr >= -30.0) & (arr <= 10.0)))

def compute_temperature_stats(arr:np.ndarray)->tuple:
    mean=round(float(np.mean(arr)),2)
    standard=round(float(np.std(arr)),2)
    max=round(float(np.max(arr)),2)
    min=round(float(np.min(arr)),2)

    return (mean,standard,max,min)

def categorize_temperature(arr:np.ndarray)->np.ndarray:
    categories=[]

    for value in arr:
        if -30.0 <= value <=-18.0:
            categories.append('Frozen')
        elif -18.0 < value <= 5.0:
            categories.append('Chilled')
        elif 5.0 <= value <=10.0:
            categories.append('warning')
        else:
            categories.append('Invalid')

    return np.array(categories)

def longest_warning_streak(arr:np.ndarray)->int:
    current=0
    longest=0

    for value in arr:
        if 5.0 <= value <= 10.0:
            current +=1
            longest=max(longest,current)
        else:
            current=0
    return longest



values = [-25.5, -20.0, -18.0, -10.5, 0.0, 4.5, 6.0, 8.5, 9.0, -22.0]

arr = create_temperature_array(values)

print("Array:", arr)
print("Valid:", validate_temperature_array(arr))
print("Statistics:", compute_temperature_stats(arr))
print("Categories:", categorize_temperature(arr))
print("Longest Warning Streak:", longest_warning_streak(arr))

    
