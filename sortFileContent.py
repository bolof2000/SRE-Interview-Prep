def getMostFrequentWords(file):

	maxWord = ""
	maxKey = 0

	ifile = open("text.txt","r")
	lines = ifile.readlines()
	word_count = {}
	for line in lines:
		words = line.split()
		print(words)

		for word in words:
			word = word.strip(".,!?:;'\"")
			word.lower()
			word_count[word] = word_count.get(word,0)+1
	#word_list = list(word_count.keys())
	#word_list.sort()

	for k in word_count:
		if word_count[k] > maxKey:
			maxKey = word_count[k]
			maxWord = k

	return maxWord

print(getMostFrequentWords("text.txt"))