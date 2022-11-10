#1: Create a function to detect and print duplicate characters from a given string
# BONUS: Modify the function to also include the number of times theduplicate character appears in the string

def duplicate_characters(string_to_check):
    # list = [string_to_check[i] for i in range(0,len(string_to_check))]
    # list.sort()
    # sorted_string = ""
    dict = {}
    # for element in list:
    #     sorted_string+=element
    # print(sorted_string) 
    for char in string_to_check:
        dict.update({char: string_to_check.count(char)})
    duplicates = {}
    for pair in dict:
        if dict[pair] > 1:
            duplicates.update({pair: dict[pair]})
    print(duplicates)

duplicate_characters("oqiwhfujisbdckjvbzxiousdibsguirbgaaaaaaaaaa")

#2: Create a function that reverses a string, utilizing recursion

def reverse_string_with_recursion(string_to_reverse):
    # reversed_string=""
    # for neg in range(len(string_to_reverse) -1, -1, -1):
    #     reversed_string += string_to_reverse[neg]
    # print(reversed_string)
    if string_to_reverse == "":
        return string_to_reverse
    else:
        return string_to_reverse[-1] + reverse_string_with_recursion(string_to_reverse[:-1])
        

test = reverse_string_with_recursion("reverse")
print(test)