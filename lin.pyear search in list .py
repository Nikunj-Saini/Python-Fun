def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
numbers = [10, 20, 30, 40, 50]
target = int(input("Enter a number to search: "))
result = linear_search(numbers, target)
if result != -1:
    print(f"Number found at index {result}.")
else:
    print("Number not found.")

