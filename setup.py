from setuptools import setup, find_packages

setup(
    name="scalify",
    version="0.1.0",  # Replace with your versioning scheme
    description="A lightweight AI engineering toolkit for building natural language interfaces that are reliable, scalable, and easy to trust.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="LICENSE",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=[
        "ai", "chatbot", "llm", "NLP", "natural language processing"
    ],
    python_requires=">=3.9",
    packages=find_packages(where="scalify"),
    install_requires=[
        "cachetools>=5",
        "readyapi",
        "httpx>=0.24.1",
        "jinja2>=3.1.2",
        "jsonpatch>=1.33",
        "openai>=1.21.0",
        "prompt-toolkit>=3.0.33",
        "pydantic>=2.4.2",
        "pydantic_settings",
        "rich>=12",
        "tiktoken>=0.4.0",
        "cligenius>=0.12.3",
        "typing_extensions>=4.0.0",
        "tzdata>=2023.3",  # Needed for Windows
        "uvicorn>=0.22.0",
        "partialjson>=0.0.5",
    ],
    extras_require={
        "generator": ["datamodel-code-generator>=0.20.0"],
        "chromadb": ["chromadb"],
        "dev": [
            "scalify[tests]",
            "black[jupyter]",
            "ipython",
            "mkdocs-autolinks-plugin~=0.7",
            "mkdocs-awesome-pages-plugin~=2.8",
            "mkdocs-markdownextradata-plugin~=0.2",
            "mkdocs-jupyter>=0.24.1",
            "mkdocs-material[imaging]>=9.1.17",
            "mkdocstrings[python]~=0.22",
            "pdbpp~=0.10",
            "pre-commit>=2.21,<4.0",
            "pydantic[dotenv]",
            "ruff",
        ],
        "tests": [
            "pytest-asyncio>=0.18.2,!=0.22.0,<0.23.0",
            "pytest-env>=0.8,<2.0",
            "pytest-rerunfailures>=10,<14",
            "pytest-sugar>=0.9,<2.0",
            "pytest~=7.3.1",
            "pytest-timeout",
            "pytest-xdist",
        ],
        "audio": [
            "SpeechRecognition>=3.10",
            "PyAudio>=0.2.11",
            "pydub>=0.25",
            "simpleaudio>=1.0",
        ],
        "video": ["opencv-python >= 4.5"],
    },
    entry_points={
        "console_scripts": [
            "scalify = scalify.cli:app"
        ],
    },
    url="https://github.com/khulnasoft/scalify",
    project_urls={
        "Code": "https://github.com/khulnasoft/scalify",
    },
    setup_requires=["setuptools>=45", "setuptools_scm[toml]>=6.2"],
    scm_version={
        "write_to": "scalify/_version.py",
    },
)
