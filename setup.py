from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str):
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    requirements = [i.replace('\n','') for i in requirements if i != HYPEN_E_DOT]
    return requirements
    

setup(name = 'end_to_end',
      version='0.1.0',
      description='machine learning projects',
      author='msarathrahul',
      author_email='test@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt'))