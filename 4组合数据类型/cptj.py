import jieba

txt = open('高瓴人工智能学院简介.txt','r',encoding='utf-8').read()

words = jieba.lcut(txt)

counts = {}

for w in words:
	if len(w) > 2:
		counts[w] = counts.get(w,0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

for i in items:
	print("{0:<10}{1:>5}".format(i[0],i[1]))