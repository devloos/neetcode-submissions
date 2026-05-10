class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]

        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for num, corr_i in count.items():
            freq[corr_i].append(num)

        result = []

        for i in range(len(nums), 1, -1):
            for num in freq[i]:
                result.append(num)

        return result[0:k]


