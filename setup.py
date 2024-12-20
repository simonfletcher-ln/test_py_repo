from setuptools import setup, find_packages
import re
import os

NAME='test-py-repo'
VERSION='0.3.0'

def normalise(name):
    return re.sub(r"[-_.]+", "-", name).lower()

name = normalise(NAME)

results = setup(
    name=name,
    version=VERSION,
    packages=find_packages(),
    install_requires=[
    ],
    author='Fletch',
    author_email='simon.fletcher@lexisnexisrisk.com',
    description='A test project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/simonfletcher-ln/test_py_repo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
    }
)

# For some reason when running in github the name is wrong...
for type, _, file in results.dist_files:
    if type == 'sdist':
        if file != f"dist/{name}-{VERSION}.tar.gz":
            print(f"Moving {file} to dist/{name}-{VERSION}.tar.gz")
            os.rename(file, f"dist/{name}-{VERSION}.tar.gz")
        print(f"GITLAB_SDIST=dist/{name}-{VERSION}.tar.gz")
    elif type == 'bdist_wheel':
        print(f"GITLAB_BDIST_WHEEL={file}")