from setuptools import setup, find_packages

setup(
    name="smart-campus-connect",
    version="1.0.0",
    author="Amanda",
    description="Smart Campus Connect - Student Lifecycle Management Platform",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
        "pydantic>=2.5.0",
        "pytest>=7.4.0",
        "httpx>=0.25.0",
    ],
    python_requires=">=3.13",
)
