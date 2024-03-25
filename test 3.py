class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items_dict = {}
        for item in items1:
            value, weight = item
            items_dict.setdefault(value, 0)
            items_dict[value] += weight

        for item in items2:
            value, weight = item
            items_dict.setdefault(value, 0)
            items_dict[value] += weight

        sorted_items = sorted(items_dict.items())
        return [[value, weight] for value, weight in sorted_items]
