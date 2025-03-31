from novel_and_chapter import *
import jieba
from collections import Counter


class TokenizedChapter(Chapter):

	def __init__(self, title, path, encoding='utf8'):
		"""
		ToknizedChapter类对象包含三个属性:
		title: 章节标题，如：第01章 风雪惊变
		content: 章节内容
		tokenized_content: 分词后的内容
		"""
		super().__init__(title, path, encoding=encoding)  # 调用父类构造函数，初始化title和content属性
		self.tokenized_content = list(jieba.tokenize(self.content))

	def word_count(self):
		"""
		以字典或Counter的形式，返回该章节词频统计的结果，注意这里我们只统计长度大于1的词
		"""

		# 代码补完部分开始
		counter = Counter()
		for item in self.tokenized_content:
			if len(item[0])>1:
				counter[item[0]]+=1
		# print(counter)
		return counter

	# 代码补完部分结束

	def most_frequent_words(self, k=5):
		"""
		实现函数，返回该章节中出现频率最高的5个词
		"""

		# 代码补完部分开始
		ls = list(self.word_count().items())
		ls.sort(key=lambda x: x[1], reverse=True)
		return ls[:k]

	# 代码补完部分结束

	# 遍历TokenizedChapter类对象会依次输出分词后的结果
	def __iter__(self):
		return iter(self.tokenized_content)

	# 使用[]能访问第key个词
	def __getitem__(self, key):
		return self.tokenized_content[key]


class TokenizedNovel(Novel):

	def __init__(self, title, path, encoding='utf8'):
		super().__init__(title, path, encoding=encoding)

	# 请补完以下代码，通过重载Novel类相应的方法
	# 使得TokenizedNovel类对象的chapters和misc属性下保存的列表内的元素为TokenizedChapter类对象
	# 代码补完部分开始

	def read_chapter(self, path):

		# 代码补完部分开始
		title = path.title().split('/')[-1].split('.')[0]
		return TokenizedChapter(title, path)


# 代码补完部分结束

if __name__ == '__main__':
	novel = TokenizedNovel('射雕英雄传', './射雕英雄传/', encoding='utf8')
	print('小说{}共包含{}章：'.format(novel.title, len(novel)))
	for chap in novel:
		print(chap.title)  # 输出章节标题
		print('==========')
		for word, count in chap.most_frequent_words(3):
			print(word, count)
		print('==========')

	print(novel[0][0:10])

	import matplotlib.pyplot as plt
	from wordcloud import WordCloud


	def draw_word_cloud(chapter):
		text = ' '.join(x[0] for x in chapter.tokenized_content if len(x[0]) > 1)
		if os.name == 'posix':  # 非windows系统加载字体
			wordcloud = WordCloud(
				background_color="white", max_words=100,
				width=800,
				height=400,
				font_path="/System/Library/fonts/PingFang.ttc"
			).generate(text)
		else:
			wordcloud = WordCloud(
				background_color="white",
				max_words=100,
				width=800,
				height=400,
				font_path=r'C:\Windows\Fonts\simhei.ttf'
			).generate(text)
		plt.imshow(wordcloud, interpolation='bilinear')
		# plt.show()
		# plt.close()


	print(novel[0].title)
	draw_word_cloud(novel[0])

	print(novel[1].title)
	draw_word_cloud(novel[1])

	print(novel[2].title)
	draw_word_cloud(novel[2])