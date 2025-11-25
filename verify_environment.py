import sys
import torch
import torchvision
import cv2
import numpy as np

print("=" * 50)
print("环境验证报告")
print("=" * 50)

# Python版本
print(f"Python版本: {sys.version}")

# PyTorch信息
print(f"PyTorch版本: {torch.__version__}")
print(f"CUDA可用: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA版本: {torch.version.cuda}")
    print(f"GPU设备: {torch.cuda.get_device_name(0)}")

# 其他关键库
print(f"Torchvision版本: {torchvision.__version__}")
print(f"OpenCV版本: {cv2.__version__}")
print(f"NumPy版本: {np.__version__}")

# 简单PyTorch测试
x = torch.rand(2, 3)
print(f"PyTorch张量运算测试: {x.shape}")

print("=" * 50)
print("环境验证完成！")