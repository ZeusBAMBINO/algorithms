class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies) 
        return [child + extraCandies >= max_candies for child in candies]
