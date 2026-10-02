from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue = deque() #first, as with everything, we initialize the queue.
    # first we push everything into the queue. 
    #we are rotating it k times. 
    #rotating it means popping it from the left, and then pushing it to the right
    #so we are going to use the operations popleft() and append()
    b=0
    for i in arr: 
        queue.append(i)
    while k >b:
        temp = queue.popleft() 
        queue.append(temp)
        b=b+1
    return(queue)
    pass

    pass


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
