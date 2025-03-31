import hashlib
import os
from collections import defaultdict


path = r"D:\Documents"
files = []

def get_all_files(d):
	files_path = os.listdir(d)
	for f in files_path:
		if os.path.isdir(os.path.join(d, f)):
			get_all_files(os.path.join(d, f))
		else:
			files.append(os.path.join(d, f))

get_all_files(path)
sha_files = defaultdict(lambda: list())
def read_and_get_sha1(file):
	sha1 = hashlib.sha1()
	with open(file, 'rb') as f:
		for chunk in iter(lambda: f.read(), b''):
			sha1.update(chunk)
		return sha1.hexdigest()


for file in files:
	sha1 = read_and_get_sha1(file)
	sha_files[sha1].append(file)


with open('sha_files.txt', 'w',encoding="utf-8") as f:
	for sha1,file in sha_files.items():
		if len(file) > 1:
			size = 0
			for fi in file:
				size+=os.path.getsize(fi)
			f.write(sha1 + ':\n')
			f.write(str(file) + '\n')
			f.write(str(size/1024) + 'kb\n')