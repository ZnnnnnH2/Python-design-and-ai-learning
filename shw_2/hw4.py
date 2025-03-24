import csv
import os.path
import jieba

dic = set()
PersonName = []

def get_dic():
	global PersonName
	with open("小作业3-4-射雕英雄传人物.txt", 'r', encoding='utf-8') as f:
		for line in f:
			dic.add(line.strip())
	PersonName = list(dic)

FileName = []
def get_all_files():
	global FileName
	FileName.append("name")
	folder_path = "./射雕英雄传"
	FileList = []
	for f in os.listdir(folder_path):
		if os.path.isfile(os.path.join(folder_path, f)):
			FileList.append(os.path.join(folder_path, f))
			FileName.append(FileList[-1].split('\\')[-1].split('.')[0])
	# print(FileList)
	return FileList

def get_words(file):
	words = []
	with open(file, 'r', encoding='utf-8') as f:
		words += jieba.lcut(f.read())
	words = list(filter(lambda x: x in dic, words))
	# print(words)
	return words

def count(words):
	word_count = {}
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
	return word_count

def save_csv():
	get_dic() # get PersonName
	FileList = get_all_files() # get FileName
	i = 1
	fin = {}
	for f in FileList:
		words = get_words(f)
		word_count = count(words)
		# print(word_count)
		for name in PersonName:
			if name in fin:
				fin[name][FileName[i]] = word_count.get(name, 0)
			else:
				fin[name] = {}
				fin[name][FileName[i]] = word_count.get(name, 0)
		i += 1

	with open("ans.csv", 'w', encoding='utf-8-sig', newline="") as f:
		writer = csv.DictWriter(f, fieldnames=FileName)
		writer.writeheader()
		for name in PersonName:
			fin[name]["name"] = name
			writer.writerow(fin[name])

jieba.load_userdict("小作业3-4-射雕英雄传人物.txt")

save_csv()