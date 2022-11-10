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
    for pair in dict:
        if dict[pair] > 1:
            print(pair +": "+ str(dict[pair]))

    
    
    



duplicate_characters("oqiwhfujisbdckjvbzxiousdibsguirbgaaaaaaaaaa")