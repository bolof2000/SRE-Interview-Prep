from heapq import heappop,heappush


def findLargestElementInArr(nums,k):
	priorityQueue = []
	for num in nums:
		heappush(priorityQueue,num)

		print(priorityQueue)

	if len(priorityQueue)>k:
		heappop(priorityQueue)
		#print(priorityQueue)

	return priorityQueue[0]


nums = [3,2,1,5,6,4]
k = 2
findLargestElementInArr(nums,k)



