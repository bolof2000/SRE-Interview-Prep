"""
Min Heap always kick out the smallest elements in the array
time complexity using heap : 0(NlogK) - this iterate over elements left up to K after heap is used
if we have used binary search: O(NlogN) - this iterates over every elements


"""
from heapq import heappop,heappush


def findKthLargest(nums,k):
	priority_queue = []
	for num in nums:
		heappush(priority_queue,num)
		print(priority_queue)

		if len(priority_queue) > k:
			heappop(priority_queue)
		#print(priority_queue)
		#print(len(nums))
		#print(len(priority_queue))

	print(priority_queue)
	#print(len(priority_queue))

	return priority_queue[0]



print(findKthLargest([3,2,1,5,6,4],3))


def solution(nums,k):
	nums.sort()
	return nums[len(nums)-k]
