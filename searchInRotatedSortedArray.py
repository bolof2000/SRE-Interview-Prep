class Solution:

	def search(self,nums,target):

		if not nums:
			return -1

		low,high = 0, len(nums)-1

		while low<=high:
			mid = (low+high)//2
			if target == nums[mid]:
				return mid

			if nums[low] <= nums[mid]:
				if nums[low]<=target<=nums[mid]:
					high = mid-1
				else:
					low = mid+1
			else:
				if nums[mid]<=target<=nums[high]:
					low = mid+1
				else:
					high = mid-1

		return -1

	def isAlienSorted(self,words,order):
		dic = {}
		for i,c in enumerate(order):
			dic[c] =i
		for i in range(len(words)-1):
			word1 = words[i]
			word2 = words[i+1]

		for k in range(min(len(word1),len(word2))):
			if word1[k] != word2[k]:
				if dic[word1[k]] > dic[word1[k]]:
					return False
				break
		else:

			if len(word1) > len(word2):
				return False

		return True



sol = Solution()
print(sol.search([4,5,6,7,0,1,2],0))
sol.isAlienSorted()