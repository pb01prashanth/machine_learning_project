from typing import List
from xml.etree.ElementTree import VERSION
from setuptools import find_packages, setup
from typing import List
REQUIREMENT_FILE_NAME = "requirements.txt"
def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines().remove("-e .")

PROJECT_NAME ="housing_predictor"
VERSION="0.0.1"
AUTHOR="Prashanth"
DESCRIPTION = "This is the first project"
PACKAGES = ["housing"]
setup(

    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description= DESCRIPTION,
    packages= find_packages(),
    install_requires =get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())