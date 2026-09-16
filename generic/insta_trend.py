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
    sum=int(np.sum(views_array))
    mean=round(float(np.mean(views_array)),2)
    max=int(np.max(views_array))

    return (sum,mean,max)

def categorize_trend_levels(views_array:np.ndarray)->np.ndarray:
    category=[]
    for i in views_array:
        if i<3000:
            category.append('Low Trend')
        elif 3000<=i<=4999:
            category.append('Moderate Trend')
        else:
            category.append('Viral Trend')

    return np.array(category)

def longest_growth_streak(views_array:np.ndarray)->int:

    n=len(views_array)
    if n==0:
        return 0
    if n==1:
        return 1

    current_streak=1
    longest_streak=1

    for i in range(1,n):
        if views_array[i] > views_array[i-1]:
            current_streak+=1
        else:
            current_streak=1
        longest_streak=max(longest_streak,current_streak)

    return longest_streak
    
def format_view_counts(views_array:np.ndarray)->np.ndarray:
    return np.array([f"{int(i):,}" for i in views_array])




# Sample data
views = np.array([1200, 3500, 1800, 5200, 7600])


print("1. create_views_array()")
print(create_views_array([1200, 3500, 1800, 5200, 7600]))


print("\n2. validate_views_array()")
print(validate_views_array(np.array([1200, 3500, -1800, 5200])))


print("\n3. compute_view_metrics()")
print(compute_view_metrics(views))


print("\n4. categorize_trend_levels()")
print(categorize_trend_levels(views))


print("\n5. longest_growth_streak()")
print(longest_growth_streak(views))


print("\n6. format_view_counts()")
print(format_view_counts(views))


# Small hidden test cases
print("\n7. Boundary value testing")
print(categorize_trend_levels(np.array([2999, 3000, 4999, 5000])))

print("\n8. Empty array validation")
print(validate_views_array(np.array([])))

print("\n9. Formatting large numbers")
print(format_view_counts(np.array([1200, 35000, 1800000])))