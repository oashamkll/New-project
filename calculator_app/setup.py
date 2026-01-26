from setuptools import setup, find_packages

setup(
    name="calculator_app",
    version="0.1.0",
    description="A beautiful calculator application built with Kivy",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "kivy==2.1.0",
    ],
    entry_points={
        'console_scripts': [
            'calculator-app=main:CalculatorApp',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)