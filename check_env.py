# -*- coding: utf-8 -*-
import sys
import importlib

REQUIRED_MODULES = [
    "torch",
    "torchvision",
    "ultralytics",
    "cv2",
    "numpy",
    "PIL",
    "tqdm",
    "paho.mqtt.client",
    "redis",
    "fastapi",
    "uvicorn",
    "ffmpeg",
    "deep_sort",  # 已修复
]

print("=" * 50)
print("  智能安防项目 - 依赖检查工具")
print("=" * 50)

missing = []
success = []

for module in REQUIRED_MODULES:
    try:
        importlib.import_module(module)
        success.append(module)
    except:
        missing.append(module)

print(f"\n✅ 已安装：{len(success)} 个")
for m in success:
    print(f"  ✔ {m}")

print(f"\n❌ 缺失：{len(missing)} 个")
for m in missing:
    print(f"  ✘ {m}")

print("\n" + "=" * 50)

if missing:
    print("⚠  缺失模块，请安装：pip install 模块名")
else:
    print("🎉 恭喜！所有依赖都已安装完成，可以直接运行项目！")

print("=" * 50)