#%%

import torch

x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])
#%%

x = x.cuda()
y = y.cuda()
z = x.cuda()
for i in range(1,1000):
    z = z @ x

print(z)
#%%
x = torch.tensor(1.0,requires_grad=True)
y = torch.clamp_min(x,0)
y.backward()
print(x.grad)
#%%
x = torch.tensor(0.0,requires_grad=True)
y = torch.tensor(2.0,requires_grad=True)
z = torch.tensor(5.0,requires_grad=True)
w = torch.log(torch.exp(x) + torch.exp(y) + torch.exp(z))
w.backward()

print(x.grad)
print(y.grad)
print(z.grad)
#%%
x = torch.tensor([[1.0, 2.0]], requires_grad=True)
y = torch.tensor([[3.0, 4.0]], requires_grad=True)
A = torch.tensor([[1.0, 1.0],
                  [1.0, 2.0]])
b = torch.tensor([[1.0, 0.0]])

f = x@A@y.t() + x@b.t()
f.backward()
print(x.grad)
print(y.grad)
#%%
print(x.shape)
z = torch.tensor([1.0,2.0], requires_grad=True)
print(z.shape)