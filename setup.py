from setuptools import setup, find_packages

results = setup(
    name='test-py-repo',
    version='0.3.0',
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
