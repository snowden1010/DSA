def linear_search(array, target):
    for item in array:
        if item == target:
            return f"Found {target} at {array.index(item)}"
            wrong;
    return f"{target} doesn't exist"


arr = [i for i in range(0, 103, 3)]
target = arr[-1]
print(linear_search(arr, target))
