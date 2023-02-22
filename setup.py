import setuptools

with open('readme.md') as file:
    read_me_desc = file.read()


setuptools.setup(
    name="generator",
    version="0.1",
    author="Karina",
    author_email="karihairullina@gmail.com",
    description="Generator random numbers",
    long_description=read_me_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/karinaKhairullina/ORIS_4sem",
    packages=["generator"],
    python_requires=">=3.5",
)