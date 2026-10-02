from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:

    best_name = "" #initialize the best name 
    highest_score = -1 #would it work with 0?
    for name, score in scores: 
        if score > highest_score:
            highest_score = score #update the highest score (not using max function im assuming)
            best_name = name #that will be the duplet with the highest score
    return best_name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
