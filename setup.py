from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(filepath) -> List[str]:
    '''
    this function will return the list of requirements'''
    requirements = []
    with open(filepath, 'r') as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="shaju",
    author_email="03318325446sm@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
