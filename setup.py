from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='nfp',
    version='0.0.4',
    description='Keras layers for machine learning on molecular structure',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NREL/nfp',  # Optional
    author='Peter St. John',
    author_email='peter.stjohn@nrel.gov',  # Optional
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(exclude=['docs', 'tests']),  # Required
    install_requires=['numpy', 'tqdm', 'keras>=2.3.0', 'tensorflow<2.0',
                      'tqdm', 'scikit-learn'],

    project_urls={
        'Source': 'https://github.com/NREL/nfp',
    },
)
