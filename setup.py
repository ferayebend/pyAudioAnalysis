from setuptools import setup
import os

setup(
    name='sciaudio',
    version='0.1',
    #long_description=__doc__,
    packages=['sciaudio'],
    #include_package_data=True,
    zip_safe=False,
    install_requires=['pyyaml', 'numpy', 'scipy', 'sklearn', 'hmmlearn', 'simplejson', 'eyed3', 'pydub'],
)
