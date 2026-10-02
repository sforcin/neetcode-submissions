from typing import List, Deque
from collections import deque

#for a queue, you append it to the right, and pop it from the left. 
#we can use [0] to access the left of the queue, and [-1] to access the right of the queue.
def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue = deque() #first, as with everything, we initialize the queue.
    # first we push everything into the queue. 
    for i in arr: 
        queue.append(i)
    print(queue)
    pass



# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
