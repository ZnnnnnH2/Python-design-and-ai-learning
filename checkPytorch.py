import torch

x = torch.rand(5, 3)
print(torch.cuda.current_device())
print(torch.cuda.device_count())
print(torch.cuda.get_device_capability())
print(torch.cuda.get_device_name(0))
print(torch.cuda.is_available())
print(x)

print(torch.__version__)