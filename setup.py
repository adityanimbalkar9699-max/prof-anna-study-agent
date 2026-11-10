from setuptools import setup, find_packages

setup(
    name="prof-anna-study-agent",
    version="1.0.0",
    author="Aditya Nimbalkar & Antigravity DeepMind Team",
    description="World-Class Academic Sovereign Agent, Assignment Verifier, Anti-AI PDF Generator, SIH Presentation Optimizer & Exam Forensics Engine",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "click>=8.0",
        "python-pptx>=1.0.0",
        "reportlab>=4.0.0",
        "matplotlib>=3.8.0",
        "streamlit>=1.30.0",
        "jinja2>=3.1.0",
    ],
    entry_points={
        "console_scripts": [
            "anna=anna.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
    ],
)
