import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="atlas",
    version="0.0.1",
    author="Atila Tech",
    author_email="info@atila.ca",
    description="Atlas is a search engine that allows you to parse a collection of URLs, index them into a database "
                "and make it searchable.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atilatech/atlas",
    packages=["atlas"],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'atlas=atlas.run_atlas:main',
        ],
    }
)
