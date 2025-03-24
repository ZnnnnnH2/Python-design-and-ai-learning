import os.path

import jieba


def get_all_files():
	folder_path = "./射雕英雄传"
	file_list = [os.path.join(folder_path,f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,f))]
	return file_list

def get_words(file_list):
	words = []
	for file in file_list:
		with open(file, 'r', encoding='utf-8') as f:
			words += jieba.lcut(f.read())
	return list(filter(lambda x: len(x) >1, words))

def max_words(words):
	wword = words[0]
	word_count = {}
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
		if word_count[word] > word_count.get(wword, 0):
			wword = word

	ans = list(word_count.items())
	ans.sort(key=lambda x: x[1], reverse=True)
	print(ans[:10])

	return wword

jieba.load_userdict("小作业3-4-射雕英雄传词典.txt")

print(max_words(get_words(get_all_files())))
