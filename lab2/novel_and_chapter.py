import os


class Chapter(object):

	def __init__(self, title, path, encoding='utf8'):
		"""
		Chapter类对象包含两个属性:
		title: 章节标题，如：第01章 风雪惊变
		content: 章节内容
		"""
		self.title = title
		self._path, self._encoding = path, encoding
		with open(self._path, 'rt', encoding=self._encoding) as fin:
			self.content = fin.read()

	# 使用print函数等方式输出时显示章节标题
	def __repr__(self):
		return self.title


class Novel(object):

	def __init__(self, title, path, encoding='utf8'):
		"""
		Novel类对象包含三个属性：
		title：小说标题，如：射雕英雄传
		chapters：小说正文章节
		misc：小说后记、附录等其他章节
		"""
		self.title = title
		self._path, self._encoding = path, encoding
		self.chapters, self.misc = self.load_chapters()

	def load_chapters(self):
		"""
		请补全这个函数，实现读取Path目录下小说的章节
		对每一章请构造一个Chapter对象，将小说正文章节加入chapters列表中；将小说后记、附录等内容加入到misc列表中返回。
		请注意:1)需要根据各章节文件名判断是否是正文章节；2）需要对小说正文章节进行排序。
		"""
		chapters, misc = [], []
		filenames = os.listdir(self._path)
		for filename in filenames:
			path = os.path.join(self._path, filename)
			ext = os.path.splitext(path)[1]
			if ext == '.txt':
				if self.is_normal_chapter(path):
					chapters.append(self.read_chapter(path))
				else:
					misc.append(self.read_chapter(path))
			chapters.sort(key=lambda x: x.title)
			misc.sort(key=lambda x: x.title)

		return chapters, misc

	def is_normal_chapter(self, path):

	# 代码补完部分开始
		if "章" in path:
			return True
		return False
	# 代码补完部分结束

	def read_chapter(self, path):

	# 代码补完部分开始
		title = path.split('/')[-1].split('.')[0]
		return Chapter(title, path)

	# 代码补完部分结束

	# 你可以自由添加辅助函数
	# 代码补完部分开始

	# 代码补完部分结束

	# 添加以下代码将使得我们可以遍历小说，每次返回正文中的一个章节
	def __iter__(self):
		return iter(self.chapters)

	# 返回小说正文的章节数量
	def __len__(self):
		return len(self.chapters)

	# 使用[]方式索引小说章节
	def __getitem__(self, key):
		return self.chapters[key]

	# 使用print函数等方式输出时显示小说标题
	def __repr__(self):
		return self.title

if __name__ == '__main__':
	novel = Novel('射雕英雄传', './射雕英雄传/', encoding='utf8')
	print('小说{}共包含{}章：'.format(novel.title, len(novel)))
	for chap in novel:
		print(chap.title)  # 输出章节标题
		print('==========')
		print(chap.content[0:chap.content.find('。')] + '...')  # 输出各章第一句话
		print('==========')

	print('\n小说{}共包含{}个额外章节：'.format(novel.title, len(novel.misc)))
	for chap in novel.misc:
		print(chap.title)  # 输出章节标题
		print('==========')
		print(chap.content[0:chap.content.find('。')] + '...')  # 输出各章第一句话
		print('==========')