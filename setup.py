import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="bohour",
    version="0.0.1",
    author="MagedSaeed",
    author_email="mageedsaeed1@gmail.com",
    description="A Python Package for abstracting Arabic Poetry Science, Aroud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MagedSaeed/bohour",
    packages=["bohour"],
    package_dir={"bohour": "bohour"},
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Text Processing :: Linguistic",
        "Natural Language :: Arabic",
        "Intended Audience :: Science/Research",
        "Environment :: Console",
    ],
    python_requires=">=3.7",
    # install_requires=[
    #     "requests",
    #     "tqdm",
    # ],
)
