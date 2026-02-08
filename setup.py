from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path : str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        req_list = file_obj.readlines()
        requirements = [req.replace("\n","") for req in req_list]

    return requirements

setup(
    name = "DiamondPricePrediction",
    version = "0.0.1",
    author = "Asheer Ahmad",
    author_email = "asheerahmadkmt@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages = find_packages()
)