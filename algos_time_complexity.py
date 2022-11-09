#1: Determine even or odd

def is_a_number_even_or_odd(number_to_be_checked):
    if number_to_be_checked % 2 == 0:
        print(True)
    else:
        print(False)

test_input = is_a_number_even_or_odd(24)
#TC: O(n) bc only one operation is performing -- a single argument is given

#2: Given a list of numbers, determine if each item in the list is lower than 100

def is_a_list_of_numbers_less_than_one_hundred(list_to_check):
    for list_item in list_to_check:
        if list_item > 100:
            return False
    return True
            

true_test_list = [45, 32, 65, 21]
false_test_list = [10, 51, 101, 67, 2]
t = is_a_list_of_numbers_less_than_one_hundred(true_test_list)
f = is_a_list_of_numbers_less_than_one_hundred(false_test_list)

print(t, f)
#TC: O(n log n) bc the for loop iteration is subdivded into a conditional statement so potentially only a percentage of the total list items need to be checked
# would run in n-time once sorted and no triple digit numbers present -- all values would then be checked
# could numerically sort and then iterate to immediately catch triple digit number, if present  

#3: Given a list of names, determine if any names are contained in the list more than once.

def check_for_repeated_names(list_of_names):
    index_number = 0
    run_time_iterator = 0
    lowercase_list_of_names = [name.lower() for name in list_of_names]
    lowercase_list_of_names.sort()
    while run_time_iterator < len(list_of_names) -1:
        index_number += 1
        run_time_iterator += 1
        if lowercase_list_of_names[index_number] == lowercase_list_of_names[index_number-1]:
            return False
    return True
        
        

names = ['ted', "AbbY", "lOu", "bri", "Sam", "abby"]
name_check = check_for_repeated_names(names)
print(name_check)
#TC: O(n log n) bc dividing the problem into sub parts  - first using a for loop to lowercase all list names before sorting them alphabetically
#then using a while loop to check for conditional value - this would run in n-time once sorted if NO duplicates are present