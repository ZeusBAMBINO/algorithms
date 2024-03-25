class Solution:
    def sortPeople(self, names, heights):
        people = list(zip(names, heights))
        sorted_people = sorted(people, key=lambda x: -x[1])
        return [name for name, _ in sorted_people]
