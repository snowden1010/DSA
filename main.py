def linear_search(array, r):
    for item in array:
        if item == r:
            return f"Found {r} at {array.index(item)}"
    return f"{r} doesn't exist"


arr = [i for i in range(0, 103, 3)]
target = arr[-1]
print(linear_search(arr, target))
