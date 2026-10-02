from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    #first we initialize the stack 
    stack=[]
    for i in arr:
        stack.append(i) # add all the elements into the stack 
        #once everything is added, we need to pop all the elements out of the stack
    while len(stack) > 0:
        arr.append(stack.pop())
       # print(stack.pop())
   # print(stack)
    pass


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
