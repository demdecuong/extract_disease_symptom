import os
from setuptools import setup, find_packages

try:
    # pip >=20
    from pip._internal.network.session import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    try:
        # 10.0.0 <= pip <= 19.3.1
        from pip._internal.download import PipSession
        from pip._internal.req import parse_requirements
    except ImportError:
        # pip <= 9.0.3
        from pip.download import PipSession
        from pip.req import parse_requirements

long_description = ''

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
try:
    reqs = [str(ir.req) for ir in install_reqs]
except:
    reqs = [str(ir.requirement) for ir in install_reqs]

VERSION = os.getenv('PACKAGE_VERSION', 'v0.0.1')[1:]

setup(
    name='ds_extraction',
    version='v0.0.3',
    description='DS Extraction is a library for extracting disease, symptom in the medical domain',
    long_description=long_description,
    include_package_data=True,
    url='https://github.com/demdecuong/extract_disease_symptom',
    packages=find_packages(),
    author='minhnp',
    author_email='v.minhng@vinbrain.net',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    install_requires=reqs,
    keywords='ds_extraction',
    python_requires='>=3.6',
    py_modules=['ds_extraction'],

)