def conv2d(im, kernel, stride=1):
	h = len(kernel)
	w = len(kernel[0])
	H = len(im)
	W = len(im[0])
	K = []
	for i in range(h):
		line = []
		for j in range(w):
			line.append(kernel[h - i - 1][w - j - 1])
		K.append(line)
	im_out = []
	for i in range(0, H, stride):
		line = []
		for j in range(0, W, stride):
			if i + h > H or j + w > W:
				break
			ans = 0
			for u in range(h):
				for v in range(w):
					ans += im[i + u][j + v] * K[u][v]
			line.append(ans)
		if len(line) > 0:
			im_out.append(line)
	return im_out


im = [[8, -1, -8, 2, 3, -9, -2, 5, 5, 5, -8],
	  [8, 2, -8, -4, 1, 7, 6, -7, 8, -4, -6],
	  [5, 7, -1, 2, 1, -7, -4, 1, -1, 1, 0],
	  [-3, 0, -2, -2, -5, -4, -7, 5, 0, -3, -1],
	  [-5, 0, 3, 1, -1, 4, 8, -2, -3, -8, 5],
	  [-2, -7, -6, -3, -3, -3, 2, 5, -7, 7, 3],
	  [8, -9, -3, 3, 0, -4, -6, -8, 6, -8, -7],
	  [-6, 0, 0, 8, 3, -6, 1, 8, -2, 2, 7],
	  [-4, -8, 6, -3, -9, 2, -5, -4, -9, 0, -5],
	  [-6, 4, -1, 0, -4, 7, 4, 5, 0, -4, -6],
	  [6, 4, 2, -4, 7, 4, 8, -5, -1, -7, -5]]

K = [[5, -3, 3, 5, 7],
	 [0, -9, 8, -8, -8],
	 [6, 6, 1, -5, 3],
	 [-3, -9, 5, 0, 1],
	 [1, -9, -6, 0, 8]]

print(conv2d(im, K, 1))
