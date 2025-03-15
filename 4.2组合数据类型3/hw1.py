import os
from collections import defaultdict
import jieba


def get_file():
	folder_path = "./射雕英雄传"
	FileList = []
	for f in os.listdir(folder_path):
		if os.path.isfile(os.path.join(folder_path, f)):
			FileList.append(os.path.join(folder_path, f))
	return FileList


def person_name():
	dic = set()
	with open("小作业3-4-射雕英雄传人物.txt", "r", encoding="utf-8") as f:
		for line in f:
			dic.add(line.strip())
	return dic


def count_words(files):
	dd = defaultdict(lambda: defaultdict(lambda: 0))
	for file in files:
		words = []
		text = open(file, "r", encoding="utf-8").read()
		for word, index, _ in jieba.tokenize(text):
			if word in personName:
				words.append((word, index))
		words.sort(key=lambda x: x[1])
		length = len(words)
		for i in range(length):
			dd[words[i][0]][words[i][0]] += 1
			l, r = i - 1, i + 1
			while l >= 0 and words[i][1] - words[l][1] <= 50:
				if words[l][0] != words[i][0]:
					dd[words[i][0]][words[l][0]] += 1
				l -= 1
			while r < length and words[r][1] - words[i][1] <= 50:
				if words[r][0] != words[i][0]:
					dd[words[i][0]][words[r][0]] += 1
				r += 1
	return dd


jieba.load_userdict("小作业3-4-射雕英雄传词典.txt")
fileList = get_file()
personName = person_name()
d = count_words(fileList)
lsp = list(personName)
with open("hw1.answer", "w", encoding="utf-8") as f:
	for main_person in lsp:
		# print(main_person)
		f.write(main_person+": "+str(d[main_person][main_person]) + "\n")
		ls = list()
		for fellow in lsp:
			if fellow == main_person:
				continue
			ls.append((fellow, d[main_person][fellow]))
		ls.sort(key=lambda x: x[1], reverse=True)
		for fellow, count in ls[:10]:
			# print("		"+fellow+": "+str(count))
			f.write("		" + fellow + ": " + str(count) + "\n")