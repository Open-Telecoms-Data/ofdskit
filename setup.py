from setuptools import find_packages, setup

setup(
    name="ofdskit",
    version="0.1.0",
    author="Open Data Services",
    author_email="code@opendataservices.coop",
    url="https://github.com/Open-Telecoms-Data/ofdskit",
    project_urls={
        "Documentation": "https://ofdskit.readthedocs.io/en/latest/",
        "Issues": "https://github.com/Open-Telecoms-Data/ofdskit/issues",
        "Source": "https://github.com/Open-Telecoms-Data/ofdskit",
    },
    description="",
    license="MIT",
    packages=find_packages(),
    long_description="",
    python_requires=">=3.7",
    install_requires=[],
    extras_require={"dev": ["pytest", "flake8", "black==22.3.0", "isort", "mypy"]},
    entry_points="""[console_scripts]
ofdskit = ofdskit.cli.__main__:main""",
)
