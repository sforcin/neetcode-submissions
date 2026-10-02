from typing import List


def create_list_of_odds(n: int) -> List[int]:
    my_list = [i for i in range(n)]
    for i in my_list: 
        if i%2 ==0:
            my_list.remove(i)
    print(my_list)
    pass


# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
