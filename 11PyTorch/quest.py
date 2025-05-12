import torch

x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
y = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
x = x.cuda()
y = y.cuda()

for i in range(10):
	x = torch.matmul(x, y)
print(x)