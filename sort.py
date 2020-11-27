from typing import List


class MergeSortData:
    list: List[int]
    list_position: int

    first_half: List[int]
    first_half_position: int

    second_half: List[int]
    second_half_position: int

    def __init__(self, list, first_half, second_half):
        self.list = list
        self.first_half = first_half
        self.second_half = second_half
        self.first_half_position = 0
        self.second_half_position = 0
        self.list_position = 0


def merge_lists_toguether(merge_sort_data: MergeSortData):

    while merge_sort_data.first_half_position < len(
        merge_sort_data.first_half
    ) and merge_sort_data.second_half_position < len(merge_sort_data.second_half):
        if (
            merge_sort_data.first_half[merge_sort_data.first_half_position]
            < merge_sort_data.second_half[merge_sort_data.second_half_position]
        ):
            merge_sort_data.list[merge_sort_data.list_position] = merge_sort_data.first_half[
                merge_sort_data.first_half_position
            ]
            merge_sort_data.first_half_position += 1
        else:
            merge_sort_data.list[merge_sort_data.list_position] = merge_sort_data.second_half[
                merge_sort_data.second_half_position
            ]
            merge_sort_data.second_half_position += 1
        merge_sort_data.list_position += 1


def merge_first_half(merge_sort_data: MergeSortData):
    while merge_sort_data.first_half_position < len(merge_sort_data.first_half):
        merge_sort_data.list[merge_sort_data.list_position] = merge_sort_data.first_half[
            merge_sort_data.first_half_position
        ]
        merge_sort_data.first_half_position += 1
        merge_sort_data.list_position += 1


def merge_second_half(merge_sort_data: MergeSortData):
    while merge_sort_data.second_half_position < len(merge_sort_data.second_half):
        merge_sort_data.list[merge_sort_data.list_position] = merge_sort_data.second_half[
            merge_sort_data.second_half_position
        ]
        merge_sort_data.second_half_position += 1
        merge_sort_data.list_position += 1


def merge_lists(list: List[int], first_half: List[int], second_half: List[int]):
    merge_sort_data = MergeSortData(list, first_half, second_half)
    merge_lists_toguether(merge_sort_data)
    merge_first_half(merge_sort_data)
    merge_second_half(merge_sort_data)


def merge_sort(list: List[int]):
    if len(list) > 1:
        middle = len(list) // 2
        first_half = list[:middle]
        second_half = list[middle:]

        # recursivelly split list in the middle
        merge_sort(first_half)
        merge_sort(second_half)

        # merge the lists ordered
        merge_lists(list, first_half, second_half)


list_to_sort = [5, 3, 2, 4, 7, 1, 0, 6]
merge_sort(list_to_sort)
print(list_to_sort)
