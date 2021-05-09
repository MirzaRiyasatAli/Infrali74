import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Infrali74",
    version="0.0.1",
    author="Mirza Riyasat Ali",
    author_email="mirzariyasatali1@gmail.com",
    description="A vein detector library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MirzaRiyasatAli/MirzaRiyasatAli.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)