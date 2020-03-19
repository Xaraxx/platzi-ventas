import random

def binary_search(sorted_data, target, low_index, high_index):
    if low_index > high_index:
        return False

    mid = (low_index + high_index)// 2

    if target == sorted_data[mid]:
        return True
    elif target < sorted_data[mid]:
        high_index = mid - 1
        return binary_search(sorted_data, target, low_index, high_index)
    else:
        low_index = mid + 1
        return binary_search(sorted_data, target, low_index, high_index)

if __name__ == "__main__":
    data = [random.randint(0,100) for i in range(10)]

    sorted_data = sorted(data)
    #data.sort()

    print(sorted_data)
    target = int(input('Which number would you like to find?'))
    low_index = 0
    high_index = len(sorted_data) - 1
    found = binary_search(sorted_data, target, low_index, high_index)

    print(found)