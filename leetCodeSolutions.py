import unittest

def isPalindroneSolution(string):

	i = 0
	rev = ""
	stack = []
	for char in string:
		stack.append(char)
		print(stack)

	while i < len(string):
		rev = rev + stack.pop()
		i +=1

	if rev == string:
		return True

	return False

	# return rev

def reverse(string):
    string = string[::-1]
    return string
def reverse(string):
	string = string[::-1]
	return string

def sentenceRev(sen):
	res = ""
	words = sen.split()
	for i in words:
		res = res+ i[::-1]
	#reverse_sen = ' '.join(reversed(words))
	#return reverse_sen
	return "".join(res)


def longestPalindromicSubstring(string):

	longest = ""

	for i in range(len(string)):
		for j in range(i,len(string)):

			substring = string[i:j+1]
			if len(substring) > longest and isPalindrome(string):
				longest = substring
	return longest


def isPalindrome(string):
	left = 0
	right = len(string)-1
	while left < right:
		if string[left] != string[right]:
			return False
		left +=1
		right -=1

	return True


def lengthOfLongestSubstring(s):

	max_len = 0
	window_start =0
	dic = []
	for i in range(len(s)):
		char = s[i]
		if char in dic and dic[char]>= window_start:
			window_start = dic[char]+1
		dic[char] = i

		max_len = max(max_len,i-window_start+1)

	return max_len


class TestProgram(unittest.TestCase):

	def test_palindrome(self):
		self.assertEqual(isPalindroneSolution("bolofinde"),"ednifolob")
print(isPalindroneSolution("aba"))
print(sentenceRev("bolofinde olusegun victor"))
