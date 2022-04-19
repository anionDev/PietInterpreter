import os
from setuptools import setup, find_packages


version = "1.0.0"


def create_wheel_file():

    productname = "PietInterpreter"

    executables_namespace = f"{productname}"

    folder_of_current_file = os.path.dirname(os.path.realpath(__file__))
    packages = [package for package in find_packages(folder_of_current_file) if not package.endswith(".Tests")]

    with open(os.path.join(folder_of_current_file, "ReadMe.md"), "r", encoding='utf-8') as file:
        long_description = file.read()

    setup(
        name=productname,
        version=version,
        description="PietInterpreter is an interpreter for Piet-programs which was originally written by Jens Bouman.",
        packages=packages,
        author="Marius Göcke",
        author_email="marius.goecke@gmail.com",
        url="https://github.com/anionDev/PietInterpreter",
        license="MIT",
        classifiers=[
            "Programming Language :: Python :: 3.10",
            "License :: OSI Approved :: MIT License",
            "Operating System :: POSIX :: Linux",
            "Operating System :: Microsoft :: Windows :: Windows 10",
            "Topic :: Terminals",
        ],
        platforms=[
            "windows10",
            "linux",
        ],
        long_description=long_description,
        long_description_content_type="text/markdown",
        install_requires=[
            "Pillow>=9.1.0",
            "numpy>=1.22.3",
            "pygubu>=0.20.1"
        ],
        entry_points={
            'console_scripts': [
                f"Piet = {executables_namespace}.piet:main",
            ],
        },
    )


create_wheel_file()
