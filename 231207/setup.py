from setuptools import setup

APP = ['Sample00.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': False,
           'includes': ['pandas', 'openpyxl', 'tk']}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
) 