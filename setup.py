# -*- encoding: UTF-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
import io

VERSION = '0.2.6'

with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

install_requires = open("requirements.txt").readlines()

setup(
    name="zhihu",  # pip 安装时用的名字
    version=VERSION,  # 当前版本，每次更新上传到pypi都需要修改
    author="liuzhijun",
    author_email="lzjun567@gmail.com",
    url="https://github.com/lzjun567/zhihu-api",
    keyworads="zhihu",
    description="zhihu api from humans",
    long_description=long_description,
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    license='MIT License',
    classifiers=[],
    install_requires=install_requires,
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        "pytest",
    ]
)
