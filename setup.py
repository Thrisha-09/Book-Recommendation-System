from setuptools import setup

with open("ReadMe.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "NovelNest"
AUTHOR_NAME = "Thrisha_K"
SRC = "src"
REQUIREMENTS = ['streamlit', 'numpy']


setup(
    name=SRC,
    version="0.0.1",
    author=AUTHOR_NAME,
    description="A Book Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="thrishakannan09@gmail.com",
    packages=[SRC],
    python_requires=">=3.12.1",
    install_requires=REQUIREMENTS
)