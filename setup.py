from setuptools import setup, find_packages
from typing import List

# HIFEN_E_DOT is for pip install -e ., not for install_requires
# So, we'll ensure it's removed from the list passed to install_requires
# Also, include potential variations like '-e .' with spaces or comments
EDITABLE_INSTALL = ('-e .', '-e . # e.g. a comment', '-e . # editable install')

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements,
    excluding editable install markers like '-e .'.
    '''
    requirements = []
    with open(file_path) as file_obj:
        lines = file_obj.readlines()
        for line in lines:
            # Remove newline characters and strip whitespace
            clean_line = line.strip()
            # Only add to requirements if it's not an editable install marker
            # and not an empty line (after stripping)
            if clean_line and not any(clean_line.startswith(marker) for marker in EDITABLE_INSTALL):
                requirements.append(clean_line)
    return requirements

setup(
    name='MLprojects',
    version='0.0.1',
    author='mahmood',
    author_email='syedmahmoodali357@gmail.com',
    packages=find_packages(), # Now using find_packages() directly
    install_requires=get_requirements('requirements.txt')
)