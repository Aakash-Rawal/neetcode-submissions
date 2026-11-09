class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for ele in nums:
            print(f"element is {ele}")
            if ele == 1:
                count += 1
                print(f"1 found, count is {count}")
            else:
                max_count = max(max_count, count)
                print(f"max_count is {max_count}")
                count = 0
                print(f"0 found, count is {count}")

        return max(max_count, count) 
        