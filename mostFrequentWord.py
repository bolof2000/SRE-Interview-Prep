from heapq import heappop,heappush

def solution(words,k):

	dic = []
	result = []
	priorityQueue = []
	for word in words:
		if word in dic:
			dic[word] +=1
		else:
			dic[word] =1

	for k in dic:
		heappush(priorityQueue,[dic[k],k])

		if len(priorityQueue)> k:
			heappop(priorityQueue)

	while priorityQueue:
		result.append(heappop(priorityQueue)[1])


words = ["i", "love", "leetcode", "i", "love", "coding"]
print(solution(words,2))