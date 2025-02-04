import time
import numpy as np
import matplotlib.pyplot as plt

def M_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    from_left = M_sort(arr[:middle])
    from_right = M_sort(arr[middle:])
    
    merged_array = []
    left_idx = right_idx = 0
    
    while left_idx < len(from_left) and right_idx < len(from_right):
        if from_left[left_idx] < from_right[right_idx]:
            merged_array.append(from_left[left_idx])
            left_idx += 1
        else:
            merged_array.append(from_right[right_idx])
            right_idx += 1
    
    merged_array.extend(from_left[left_idx:])
    merged_array.extend(from_right[right_idx:])
    
    return merged_array

GivenData = [5, 2, 4, 7, 1, 3, 2, 6]
SortedArray = M_sort(GivenData)
print(SortedArray)

for_sizes = list(range(10, 1001, 50))
Time = []

for size in for_sizes:
    sample_array = np.random.randint(0, 10000, size).tolist()
    start_time = time.time()
    M_sort(sample_array)
    end_time = time.time()
    Time.append(end_time - start_time)

plt.figure(figsize=(8, 5))
plt.plot(for_sizes, Time, marker="o", linestyle="-", color="r", label="M_sort Time")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Graph having time on Y-axis and n on X-axis")
plt.legend()
plt.grid()
plt.show()
