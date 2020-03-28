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
			#print(heappop(max_Heap)[0])
		return result

	def mostFrequentElement(self,nums):
		dic = {}
		result = []
		for num in nums:
			if num in dic:
				dic[num] +=1
			else:
				dic[num] =1


		return result


sol = Solution()
#points = [[1,3],[-2,2],[3,3]]
#k = 1
#print(sol.KClosestPointSolution(points,k))

print(sol.mostFrequentElement([1,1,1,2,3,4,5,6,7,7,7,7]))


