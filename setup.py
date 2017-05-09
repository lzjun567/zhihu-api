from setuptools import setup

setup(
    name="zhihu",

    packages=[
        "zhihu",
        "zhihu.models"
    ],
    include_package_data=True,
    install_requires=[

        "pytest-runner",
        "requests",
        "beautifulsoup4"
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        "pytest"
    ]
)
