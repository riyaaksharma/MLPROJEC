from setuptools import find_packages,setup  #This line imports tools from setuptools that help automatically find Python packages in your project and use them to build or install your package.


Hypen_e_Dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]


        if Hypen_e_Dot in requirements:
            requirements.remove(Hypen_e_Dot)
    return requirements


setup(
    name='MLPRO',
    version='0.0.1',
    author='Riya',
    author_email='sharmariya5005@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')


)