from setuptools import setup
import zhihu
from setuptools import find_packages
import io

with io.open("README.md", encoding="utf8") as f:
    readme = f.read()

install_requires = open("requirements.txt").readlines()

setup(
    name="zhihu-api",
    version=zhihu.__version__,
    author=zhihu.__author__,
    author_email="lzjun567@gmail.com",
    url="https://github.com/lzjun567/zhihu-api",
    packages=find_packages(),
    keyworads="zhihu",
    description="zhihu api from humans",
    long_description=readme,
    # packages=[
    #     "zhihu",
    #     "zhihu.models"
    # ],
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 0 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],

    install_requires=install_requires,
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        "pytest",
    ]
)
