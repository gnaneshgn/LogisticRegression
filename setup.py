from setuptools import setup,find_packages
from typing import List
REQU_FILE_NAME="requirements.txt"

def get_packages_list()->List[str]:
    """
        This function returns list of packages in string
    """
    with open(REQU_FILE_NAME) as requiremets:
        requiremets.readlines().remove('-e .')


setup(
    name="logistic_regression_scratch",
    version="0.0.1",
    description="Logistic regression model from scratch",
    packages=find_packages(),
    license="Apacne license version 2.0",
    install_requires=get_packages_list()
)