from heapq import heappop,heappush
class Solution:

	def KClosestPointSolution(self,points,k):

		max_Heap = []

		for sub_arr in points:
			x = sub_arr[0]
			y = sub_arr[1]
			distance = -(x*x+y*y)

			heappush(max_Heap,[distance,sub_arr])
			print(max_Heap)

			if len(max_Heap) > k:
				heappop(max_Heap)
				print(max_Heap)

		result = []
		while max_Heap:
			result.append(heappop(max_Heap)[1])
		return result

	def mostFrequentElement(self,nums):
		dic = {}
		result = []
		for num in nums:
			if num in dic:
				dic[num] +=1
			else:
				dic[num] =1

		sortedKey =  list(dic.keys())
		sortedKey.sort()
		result.append(sortedKey[len(sortedKey)-1])
		result.append(sortedKey[len(sortedKey)-2])


sol = Solution()
points = [[1,3],[-2,2]]
k = 1
print(sol.KClosestPointSolution(points,k))


