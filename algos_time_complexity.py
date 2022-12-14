import time

#1: Determine even or odd

def is_a_number_even_or_odd(number_to_be_checked):
    start = time.time()
    if number_to_be_checked % 2 == 0:
        print(True)
        end = time.time()
    else:
        print(False)
        end = time.time()
    time_elapsed = (f"#1 run time: {end - start}")
    print(time_elapsed)

test_input = is_a_number_even_or_odd(2423)
#TC: O(n) bc only one operation is performing -- a single argument is given

#2: Given a list of numbers, determine if each item in the list is lower than 100

def is_a_list_of_numbers_less_than_one_hundred(list_to_check):
    start = time.time()
    for list_item in list_to_check:
        if list_item > 100:
            end = time.time()
            time_elapsed = (f"#2 False run time: {end - start}")
            print(time_elapsed)
            return False
    end = time.time()
    time_elapsed = (f"#2 True run time: {end - start}") 
    print(time_elapsed)  
    return True
            

true_test_list = [45, 32, 65, 21]
false_test_list = [10, 51, 101, 67, 2]
t = is_a_list_of_numbers_less_than_one_hundred(true_test_list)
print(t)
f = is_a_list_of_numbers_less_than_one_hundred(false_test_list)
print(f)
#TC: O(n log n) bc the for loop iteration is subdivded into a conditional statement so potentially only a percentage of the total list items need to be checked
# would run in n-time once sorted and no triple digit numbers present -- all values would then be checked
# could numerically sort and then iterate to immediately catch triple digit number, if present  

#3: Given a list of names, determine if any names are contained in the list more than once.

def check_for_repeated_names(list_of_names):
    start = time.time()
    index_number = 0
    run_time_iterator = 0
    lowercase_list_of_names = [name.lower() for name in list_of_names]
    lowercase_list_of_names.sort()
    while run_time_iterator < len(list_of_names) -1:
        index_number += 1
        run_time_iterator += 1
        if lowercase_list_of_names[index_number] == lowercase_list_of_names[index_number-1]:
            end = time.time()
            time_elapsed = (f"#3 False run time: {end - start}")
            print(time_elapsed)
            return False
    end = time.time()
    time_elapsed = (f"#3 True run time: {end - start}")
    print(time_elapsed)
    return True
        
        

names = ['ted', "Ann", "lOu", "bri", "Sam", "anN"]
name_check = check_for_repeated_names(names)
print(name_check)
#TC: O(n log n) bc dividing the problem into sub parts  - first using a for loop to lowercase all list names before sorting them alphabetically
#then using a while loop to check for conditional value - this would run in n-time once sorted if NO duplicates are present

#4: Given a list of numbers, manually sort the list into ascending order (may not use built in .sort() method).

def manual_numerical_ascending_sort(list_to_be_sorted):
    list_length = len(list_to_be_sorted)-1
    for first_index in range(list_length):
        for second_index in range(list_length-1):
            if list_to_be_sorted[second_index] < list_to_be_sorted[second_index+1]:
                list_to_be_sorted[second_index], list_to_be_sorted[second_index+1] = list_to_be_sorted[second_index+1], list_to_be_sorted[second_index]
    return list_to_be_sorted

number_list = [21, 45, 98, 61, 2]
ascending_sort = manual_numerical_ascending_sort(number_list)  
print(ascending_sort)
#TC: O(n^2) bc there are two nested for loops so it could potentially run for len(argument)^2
