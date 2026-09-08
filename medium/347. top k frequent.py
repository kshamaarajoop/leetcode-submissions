class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        res = []
        for i, num in enumerate(nums):
            hMap[num] = hMap.get(num,0)+1
        sorted_dict_by_values = dict(sorted(hMap.items(), key=lambda item: item[1]))
        print(sorted_dict_by_values)
        
        return list(sorted_dict_by_values.keys())[-k:]
        print(list(sorted_dict_by_values.keys())[-k:])
