#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/3 0:21
# @Author  : yszar
# @FileName: setup.py.py
# @Blog    : https://iamjy.com
# @Contact : yszaryszar@gmail.com
# @Version : 1.0.0
# !/usr/bin/env python"
# -*-coding:utf-8 -*-"

from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="obsidian-vuepress",  # 包名
    version="0.0.1",  # 版本号
    description="Convert prompt blocks in obsidian notes when they are published to vuepress",
    long_description=long_description,
    author="Jiu Yang",
    author_email="yszaryszar@gmail.com",
    url="https://iamjy.com",
    python_requires=">=3",
    install_requires=[],
    license="MIT License",
    packages=find_packages(),
    platforms=["all"],
    setup_requires=["pbr"],
    pbr=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
    ],
    # 用来支持自动生成脚本，安装后会自动生成 /usr/bin/obsidian-vuepress 的可执行文件
    # 该文件入口指向 obsidian-vuepress/main.py 的main 函数
    entry_points={
        "console_scripts": ["obsidian-vuepress = obsidian-vuepress.main:main"]
    },
    # 将 bin/foo.sh 和 bar.py 脚本，生成到系统 PATH中
    # 执行 python setup.py install 后
    # 会生成 如 /usr/bin/foo.sh 和 如 /usr/bin/bar.py
    # scripts=["bin/foo.sh", "bar.py"],
)
