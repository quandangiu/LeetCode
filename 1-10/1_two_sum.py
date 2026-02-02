from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		num_map = {}
		for i, num in enumerate(nums):
			complement = target - num
			if complement in num_map:
				return [num_map[complement], i]
			num_map[num] = i
		return []
def two_sum(nums, target):
	"""
	Trả về chỉ số của hai số trong mảng nums sao cho tổng của chúng bằng target.
	Sử dụng hash map để đạt O(n) thời gian.
	"""
	num_map = {}
	for i, num in enumerate(nums):
		complement = target - num
		if complement in num_map:
			return [num_map[complement], i]
		num_map[num] = i
	return []  
# Ví dụ sử dụng
if __name__ == "__main__":
	print(two_sum([2,7,11,15], 9))    # [0, 1]
	print(two_sum([3,2,4], 6))        # [1, 2]
	print(two_sum([3,3], 6))          # [0, 1]
