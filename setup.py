import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Attr-Dict",
    version="1.0.0",
    author="LuckyDams",
    author_email="LuckyDams@gmail.org",
    description="Yet another Attribute Dict implementation !",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LuckyDams/Attr-Dict",
    license="MIT",
    packages=setuptools.find_packages(exclude=("tests",)),
    # include_package_data=True,
    platforms='any',
    zip_safe=True,
    python_requires='>=3.4',
    install_requires=[],
    # test_suite="tests",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
