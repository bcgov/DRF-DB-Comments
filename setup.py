import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ldf_drf_db_comments",
    version="0.0.1",
    author="Robert Johnstone, Matthew Hall",
    author_email="matthew.hall@gov.bc.ca",
    description="A module of the Living Documentation Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bcgov/ldf_drf_db_comments",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
)
