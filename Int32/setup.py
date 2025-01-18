from setuptools import setup, Extension

# 定义模块
module = Extension(
    "myctypes",
    sources=["myctypes.c"],
)

# 设置包信息
setup(
    name="myctypes",
    version="1.0",
    description="module 编写示范",
    ext_modules=[module],
)
