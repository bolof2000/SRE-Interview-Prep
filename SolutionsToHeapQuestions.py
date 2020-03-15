from heapq import heappush,heappop

class Solution:

	def topKMostFrequentElement(self,nums,k):
		priority_Queue = []
		dic = {}

		for num in nums:
			if num in dic:
				dic[num] +=1
			else:
				dic[num] =1

		for key in dic.keys():
			val = dic[key]
			#print(val)
			number = key
			print(number)
			heappush(priority_Queue,[val,number])
			#print(priority_Queue)
			if len(priority_Queue)> k:
				heappop(priority_Queue)

				#print(priority_Queue)
				#print(dic)
		result = []
		while priority_Queue:
			result.append(heappop(priority_Queue)[1])
			#print(heappop(priority_Queue))
			#print(heappop(priority_Queue)[1])

		#print(priority_Queue)

		return  result

	def topKFrequent(self,words,k):

		result = []
		dic = {}
		priority_queue = []
		



sol = Solution()
print(sol.topKMostFrequentElement([1,1,1,2,2,3],1))





