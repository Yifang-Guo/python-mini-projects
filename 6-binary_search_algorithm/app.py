# a function that takes a list and target parameter
def binary_search(list, element):
    mid = 0
    start = 0
    end = len(list) - 1
    steps = 0

    while start <= end:
        print(f"steps: {steps}: {list[start:end+1]}")

        steps += 1
        mid = start + (end - start) // 2

        if element == list[mid]:
            return mid
        
        if element < list[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1

list = [2, 4, 5, 6, 8, 12, 45]

index = binary_search(list, 2)

if index != -1:
    print(f"found the element at {index}")
else:
    print("element not found in the list")