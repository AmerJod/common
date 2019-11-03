import setuptools

with open("requirements.txt", "r") as rf:
    reqs = [i for i in rf.readlines()]

setuptools.setup(
    name="spiderlib",
    version="0.0.1",
    author="Amer Joudiah",
    packages=setuptools.find_packages(),
    requirements=reqs
)