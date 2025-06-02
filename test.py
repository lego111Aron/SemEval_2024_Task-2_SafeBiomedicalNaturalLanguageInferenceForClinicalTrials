import torch
print("CUDA available:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")


import torch
import accelerate
import transformers

print(torch.__version__)
print(accelerate.__version__)
print(transformers.__version__)
