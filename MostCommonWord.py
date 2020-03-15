import re
def most_common_word(paragraph,banned):
	banned_unique = set()
	result = ""
	maxKey = 0
	count_words= {}
	for string in banned:
		banned_unique.add(string)

	new_sentence = re.sub(r"[^A-Za-z]",' ',paragraph).lower().split("\n")
	#print(new_sentence)
	for word in new_sentence:
		if word not in banned_unique:
			if word in count_words:
				count_words[word] +=1
			else:
				count_words[word] =1
	print(count_words)

	for k in count_words:
		#print(k)
		if count_words[k] > maxKey:
			maxKey = count_words[k]
			result = k

	return result


para = "bolofinde, bolofinde ,bolofinde olusegun victor test engineer visa , nigeria boy, olusegun visa, visa visa visa visa "
banned = " bolofinde,test"
print(most_common_word(para,banned))





