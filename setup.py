from setuptools import setup, find_packages

setup(
    name="tpv-core",
    version="42.0.0",
    author="Slarti Bartfast & Mark Weatherill",
    description="A formal algorithmic model exploring the is/ought boundary condition via negative utilitarian ethics.",
    long_description_content_type="text/markdown",
    url="https://substack.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
