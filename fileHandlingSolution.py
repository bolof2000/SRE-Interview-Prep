import re
from heapq import heappop,heappush
class Solution:

	def countFileContent(self, file,K):
		"""
		 Open the file and read lines
		 close file
		 strip white spaces
		 split to convert to array

		"""
		dic = {}
		openfile = open(file,'r')
		content = openfile.read()
		openfile.close()
		content_clean = re.sub('[^A-Za-z0-9]', ' ', content)
		content_split = content_clean.strip().split()
		for word in content_split:
			dic[word] = dic.get(word,0)+1
		#print(dic)

		largest = -1
		most_frequent_word = None
		for k,v in dic.items():
			if v > largest:
				largest = v
				most_frequent_word = k
		print(largest)
		print(most_frequent_word)

		result = []
		queue = []
		for keys in dic.keys():
			#print((dic[keys]))
			#print(keys)
			heappush(queue,[dic[keys],keys])
			if len(queue) > K:
				heappop(queue)

		while queue:
			result.append(heappop(queue)[0])

		return result


sol = Solution()
print(sol.countFileContent("employee.json",1))
