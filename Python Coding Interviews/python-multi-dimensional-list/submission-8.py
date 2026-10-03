from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    maximum =0 #first, we initialize the maximum
    max_arr = []
    for sublist in nested_arr: #for each sublist in the nested array
    #for each sublist, we need to find the maximum of it
        maximum = max(sublist) 
        max_arr.append(maximum)
        
    return(max_arr)
    pass


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
