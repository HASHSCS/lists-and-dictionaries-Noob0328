# TODO: Implement a function that returns a list of numbers from 1 to n
def generate_numbers(n):

    number=list(range(1, n+1))
    return number 



# TODO: Implement a function that returns a dictionary where keys are numbers from 1 to n and values are their squares
def generate_squares(n):
    squares_dict = {}
    for number in range(1, n+1):
        squares_dict[number] =number**2
    return squares_dict


# TODO: Implement a function that merges two lists in an alternating fashion
def merge_lists(list1, list2):
    merged_list = []
    min_len = min(len(list1), len(list2))
    for i in range(min_len):
        merged_list.append(list1[i])
        merged_list.append(list2[i])
    merged_list.extend(list1[min_len:])
    merged_list.extend(list2[min_len:])
    return merged_list

# TODO: Implement a function that returns a list and replicates the dictionary keys based on their respective values
def multiply_keys(data):
    multiplied_keys = []
    for key, value in data.items():
        multiplied_keys.extend([key] * value)
    return multiplied_keys
# TODO: Implement a function that converts a list of strings to a dictionary with the string as the key and its length as the value
def list_to_dict(items):
    dictionary = {}
    for item in items:
        dictionary[item] = len(item)
    return dictionary

# TODO: Implement a function to find the majority element in a list
def majority_element(nums):
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate
# TODO: Implement a function that filters a dictionary based on a threshold value. If the value of any key in the dictionary is greater than the threshold, that key-value pair should be retained in the output dictionary. Otherwise, it should be excluded.
def filter_dictionary(data, threshold):
    
    filtered_data = {key: value for key, value in data.items() if value > threshold}
    return filtered_data