import random
from time import time

def time_execution(func):
    '''
    Run the provided function `func` and log the time execution

    arguments:
    func -- the function to run
    '''
    def wrapper(*args, **kwargs):
        start = time()
        func_output = func(*args, **kwargs)
        end = time()
        time_execution = end - start
        print(f'{func.__name__} takes {time_execution:.7f}')
        return func_output
    return wrapper

# SEARCH
@time_execution
def binary_search(search_list: list[int], search_element: int):
    low_id = 0
    high_id = len(search_list) - 1
    attempt = 0
    while low_id <= high_id:
        mid_id = ( high_id + low_id ) // 2
        mid_element = search_list[mid_id]
        attempt += 1
        if  mid_element == search_element:
            return attempt, mid_id
        elif mid_element > search_element:
            high_id = mid_id - 1
        elif mid_element < search_element:
            low_id = mid_id + 1
    return attempt, None

@time_execution
def simple_search(search_list: list[int], search_element: int):
    attempt = 0
    for _element_id, element in enumerate(search_list):
        attempt += 1
        if element == search_element:
            return attempt, _element_id
    return attempt, None

# RECURSION
def get_sum_by_recursion(list_to_sum: list[int]):
    if len(list_to_sum) == 0:
        return 0
    else:
        return list_to_sum[0] + get_sum_by_recursion(list_to_sum[1:])

def get_list_len(list_to_get_len: list[int]):
    if list_to_get_len == []:
        return 0
    else:
        return 1 + get_list_len(list_to_get_len[1:])

def get_list_max(list_to_get_max: list[int]):
    if len(list_to_get_max) == 1:
        return list_to_get_max[0]
    else:
        return list_to_get_max[0] if list_to_get_max[0] > get_list_max(list_to_get_max[1:]) else get_list_max(list_to_get_max[1:])

# SORT
@time_execution
def selection_sort(list_to_sort: list[int]):

    def find_the_smallest(search_list: list[int]):
        smallest_element_id = 0
        for elm_id, element in enumerate(search_list):
            smallest_element_id = elm_id if element < search_list[smallest_element_id] else smallest_element_id
        return smallest_element_id

    sorted_list = []
    list_to_sort_copy = list_to_sort[:]
    while len(list_to_sort_copy) != 0:
        smallest_element_id = find_the_smallest(list_to_sort_copy)
        sorted_list.append(list_to_sort_copy.pop(smallest_element_id))
    return sorted_list

# @time_execution
def quick_sort(list_to_sort: list[int]):
    len_list_to_sort = len(list_to_sort)
    if len_list_to_sort < 2:
        return list_to_sort
    else:
        random_pivot_point = list_to_sort[random.choice(range(len_list_to_sort))]
        less_pivot_point = [i for i in list_to_sort if i < random_pivot_point]
        pivot_point = [i for i in list_to_sort if i == random_pivot_point]
        larger_pivot_point = [i for i in list_to_sort if i > random_pivot_point]
        return quick_sort(less_pivot_point) + pivot_point + quick_sort(larger_pivot_point)

@time_execution
def buble_sort(list_to_sort: list[int]):
    for i in range(len(list_to_sort) - 1):
        for j in range(len(list_to_sort) - i - 1):
            if list_for_sort[j] > list_to_sort[j + 1]:
                list_for_sort[j], list_to_sort[j + 1] = list_for_sort[j + 1], list_to_sort[j]
    return list_to_sort

if __name__ == "__main__":
    # # SEARCH examples::
    max_element = pow(2, 10)
    element_to_search = random.choice(range(max_element))
    bin_attempts, bin_search_id = binary_search(range(max_element + 1), element_to_search)
    simple_attempts, simple_search_id = simple_search(range(max_element + 1), element_to_search)
    if bin_search_id != simple_search_id:
        print(f'ERROR:: searching algorithms retun different result: {bin_search_id =} != {simple_search_id =}')

    # # RECURSION examples::
    list_for_recursion = [1, 2, 3, 40, 0, 8, 9, 88]
    list_len = get_list_len(list_for_recursion)
    if list_len != len(list_for_recursion):
        print(f'ERROR:: get_list_len return {list_len = }')
    list_sum = get_sum_by_recursion(list_for_recursion)
    if list_sum != sum(list_for_recursion):
        print(f'ERROR:: get_sum_by_recursion return {list_sum = }')
    list_max = get_list_max(list_for_recursion)
    if list_max != max(list_for_recursion):
        print(f'ERROR:: get_list_max return {list_max = }')

    # # SORT examples::
    list_for_sort = [ random.choice(range(100000)) for i in range(100) ]
    sorted_list = sorted(list_for_sort)
    sorted_list1 = selection_sort(list_for_sort)
    sorted_list2 = quick_sort(list_for_sort)
    sorted_list3 = buble_sort(list_for_sort)
    if sorted_list1 != sorted_list \
        or sorted_list2 != sorted_list\
        or sorted_list3 != sorted_list:
        print(f'ERROR:: sorting algorithms result: {sorted_list1 = } {sorted_list2 = } {sorted_list3 = }')
