from collections import defaultdict
from tokenized_chapter_and_novel import *


class TokenizedChapterWithCharacter(TokenizedChapter):

	def __init__(self, title, path, novel_characters, encoding='utf8'):
		"""
		ToknizedChapter类对象包含四个属性:
		title: 章节标题，如：第01章 风雪惊变
		content: 章节内容
		tokenized_content: 分词后的内容
		characters: 本章出现的人物的列表
		character_positions: 一个dict，key为人物名称，value为一个list保存本章人物出现的位置（是第几个词）
		"""
		super().__init__(title, path, encoding=encoding)  # 调用父类构造函数
		self.characters, self.character_positions = self.get_character_count(novel_characters)

	# 补完代码，正确的根据novel_characters中的人物信息，初始化characters和character_positions属性
	# 代码补完部分开始

	# 代码补完部分结束

	def get_character_count(self, character_name):

		# 请补完以下函数，返回人物在章节中出现的次数
		# 代码补完部分开始
		character_positions = defaultdict(list)
		characters = []
		length = len(self.tokenized_content)
		for i in range(length):
			if self.tokenized_content[i][0] in character_name:
				if character_positions[self.tokenized_content[i][0]] is None:
					characters.append(self.tokenized_content[i][0])
				character_positions[self.tokenized_content[i][0]].append(i)
		return characters, character_positions

	# 代码补完部分结束

	def find_character(self, character_name, k=0):

		# 请补完以下函数，返回人物在该章节第k次出现的上下文，并且在人物名称周围加上*，例如：*郭靖*
		# 代码补完部分开始
		position = self.character_positions[character_name][k]
		ls = list()
		ls.extend(self.tokenized_content[position - 20:position])
		ls.append(("*" + character_name + "*",None))
		ls.extend(self.tokenized_content[position + 1:position + 21])
		return ''.join([x[0] for x in ls])


# 代码补完部分结束


class TokenizedNovelWithCharacter(TokenizedNovel):
	def __init__(self, title, path, character_file_path, encoding='utf8'):
		"""
		TokenizedNovelWithCharacter类对象包含四个属性：
		title：小说标题，如：射雕英雄传
		chapters：小说正文章节
		misc：小说后记、附录等其他章节
		characters：一个list，保存小说中出现的所有人物名称
		"""
		# 补完代码，打开保存人物名称的文件，初始化characters属性
		# 代码补完部分开始
		characters = []
		with open(character_file_path, 'r', encoding=encoding) as f:
			for line in f:
				line = line.strip()
				if line != '':
					characters.append(line)
		self.characters = characters
		# 代码补完部分结束

		# 初始化jieba分词，并将人物名称作为自定义词加入词典
		jieba.initialize()
		for c in self.characters:
			jieba.add_word(c, freq=1024)

		super().__init__(title, path, encoding=encoding)

	# 请补完以下代码，通过重载TokenizedNovel类相应的方法
	# 使得TokenizedNovelWithCharacter类对象的chapters和misc属性下
	# 保存的列表内的元素为TokenizedChapterWithCharacter类对象
	# 代码补完部分开始
	def read_chapter(self, path):

		# 代码补完部分开始
		title = path.title().split('/')[-1].split('.')[0]
		return TokenizedChapterWithCharacter(title, path, self.characters)

	# 代码补完部分结束

	def character_count_in_chapter(self, character_name, chapter_index):
		# 请补完以下函数，返回人物在指定章节中出现的次数
		# 代码补完部分开始
		return self.chapters[chapter_index].character_positions[character_name].__len__()

	# 代码补完部分结束

	def character_count(self, character_name):

		# 请补完以下函数，返回人物在整部小说中出现的次数
		# 代码补完部分开始
		count = 0
		for chapter in self.chapters:
			count += chapter.character_positions[character_name].__len__()
		# for chapter in self.misc:
		# 	count += chapter.character_positions[character_name].__len__()
		return count

	# 代码补完部分结束

	def find_character_in_chapter(self, character_name, chapter_index, k=0):

		# 请补完以下函数，返回人物在某个章节第k次出现的上下文
		# 代码补完部分开始
		return self.chapters[chapter_index].find_character(character_name, k)

	# 代码补完部分结束

	def find_character(self, character_name, k=0):

		# 请补完以下函数，返回人物在整部小说中第k次出现的上下文,和所在章节
		# 代码补完部分开始
		count = -1
		for chapter in self.chapters:
			count += chapter.character_positions[character_name].__len__()
			if count >= k:
				return chapter.find_character(character_name, k - (
							count - chapter.character_positions[character_name].__len__() + 1)), chapter.title


# 代码补完部分结束


if __name__ == '__main__':
	novel = TokenizedNovelWithCharacter('射雕英雄传', './射雕英雄传/', './射雕英雄传人物.txt', encoding='utf8')
	# 输出人物在小说中出现的次数，并从高到低排序
	character_counts = sorted(
		[(c, novel.character_count(c)) for c in novel.characters],
		key=lambda x: x[1],
		reverse=True
	)
	for c, count in character_counts:
		print('{:4} : {}'.format(c, count))

	# 输出各个人物出现的次数(作业4）
	for c in novel.characters:
		print(c, end=',')
		print(
			','.join(
				str(novel.character_count_in_chapter(c, chap_idx)) for chap_idx in range(len(novel)))
		)

	c = '郭靖'
	print(c, end=',')
	print(
		','.join(
			str(novel.character_count_in_chapter(c, chap_idx)) for chap_idx in range(len(novel))
		)
	)

	# 郭靖在第一章中第一次出现
	print('第一章第一次:...{}...'.format(novel.find_character_in_chapter('郭靖', 0, k=0)))
	# 郭靖在第一章中第二次出现
	print('第一章第二次:...{}...'.format(novel.find_character_in_chapter('郭靖', 0, k=1)))

	# 郭靖在第三章中第一次出现
	print('第三章第一次:...{}...'.format(novel.find_character_in_chapter('郭靖', 2, k=0)))
	# 郭靖在第三章中第二次出现
	print('第三章第二次:...{}...'.format(novel.find_character_in_chapter('郭靖', 2, k=1)))

	# 黄蓉第一次出现
	print('{1}: \n...{0}...'.format(*novel.find_character('黄蓉')))

	# 东邪西毒北丐南帝第一次出现
	print('{1}: \n...{0}...'.format(*novel.find_character('黄药师')))
	print('{1}: \n...{0}...'.format(*novel.find_character('欧阳锋')))
	print('{1}: \n...{0}...'.format(*novel.find_character('洪七公')))
	print('{1}: \n...{0}...'.format(*novel.find_character('一灯大师')))
