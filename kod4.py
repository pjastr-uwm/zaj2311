from typing import List

def sum(a: List[List[int]], b:List[List[int]]) -> List[List[int]]:
    wynik: List[List[int]] = []
    for i in range(0, len(a)):
        c = [x + y for x, y in zip(a[i], b[i])]
        wynik.append(c)

    return wynik


a: List[List[int]] = [[3, 4, 1], [1, 1, 1]]
b: List[List[int]] = [[1, 1, 1], [-2, -2, -2]]
print(sum(a, b))
