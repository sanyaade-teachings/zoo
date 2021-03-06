from setuptools import find_packages, setup


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="larq-zoo",
    version="2.0.5",
    author="Plumerai",
    author_email="opensource@plumerai.com",
    description="Reference implementations of popular Binarized Neural Networks",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/plumerai/larq-zoo",
    packages=find_packages(),
    license="Apache 2.0",
    install_requires=[
        "numpy~=1.15",
        "larq>=0.9.2,<0.11.0",
        "zookeeper>=1.0",
        "importlib-metadata ~= 2.0 ; python_version<'3.8'",
    ],
    extras_require={
        "tensorflow": ["tensorflow>=1.15.0"],
        "tensorflow_gpu": ["tensorflow-gpu>=1.15.0"],
        "test": [
            "black==20.8b1",
            "flake8>=3.7.9,<3.9.0",
            "isort==5.7.0",
            "pytype==2020.10.8",
            "pytest>=4.3.1",
            "pytest-cov>=2.6.1",
            "pytest-mock>=3.1.1",
            "pytest-xdist==2.2.0",
            "Pillow==8.1.0",
            "tensorflow_datasets>=3.1.0",
        ],
    },
    entry_points="""
        [console_scripts]
        lqz=larq_zoo.training.main:cli
    """,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
    ],
)
