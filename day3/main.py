from functools import reduce
from operator import mul


def openfile(file: str) -> list[str]:
    with open(file) as file:
        return [line.rstrip() for line in file]


def task():
    grid = openfile("input.txt")
    temp_num = ""
    numbers = []
    adjacent_index = set()
    gear_coords = set()
    for i in range(len(grid[0])):
        for l in range(len(grid)):
            index = grid[i][l]
            if not index.isdigit() and index != ".":
                gear_coords.add((i, l))  # Store location of gears in a set
            if index.isdigit():
                temp_num += index
                for coords in [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]:
                    adjacent_index.add((i + coords[0], l + coords[1]))
            else:
                if temp_num:
                    n = int(temp_num)
                    numbers.append((n, adjacent_index))
                    temp_num = ""
                    adjacent_index = set()

    multi_gear = set()
    for gear in gear_coords:
        an = [num for num, adj in numbers if gear in adj]
        if len(an) >= 2:
            multi_gear.add(reduce(mul, an))

    print(sum([num[0] for gear in gear_coords for num in numbers if gear in num[1]])) #task 1
    print(sum(multi_gear)) #task 2


if __name__ == "__main__":    
    task()
    
