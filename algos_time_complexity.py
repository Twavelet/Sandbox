#1: Determine even or odd

def is_a_number_even_or_odd(number_to_be_checked):
    if number_to_be_checked % 2 == 0:
        print(True)
    else:
        print(False)

test_input = is_a_number_even_or_odd(24)
#TC: O(n)

#2: Given a list of numbers, determine if each item in the list is lower than 100

def is_a_list_of_numbers_less_than_one_hundred(list_to_check):
    for list_item in list_to_check:
        if list_item > 100:
            return False
    return True
            

true_test_list = [45, 32, 65, 21]
false_test_list = [10, 51, 1, 67, 2]
t = is_a_list_of_numbers_less_than_one_hundred(true_test_list)
f = is_a_list_of_numbers_less_than_one_hundred(false_test_list)

print(t, f)
#TC: O(log n)
