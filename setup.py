
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='fastocr',
    version='0.2.0',
    description='FastOCR is a desktop application for OCR API.',
    python_requires='<3.10,>=3.7',
    project_urls={"documentation": "https://github.com/BruceZhang1993/FastOCR", "homepage": "https://github.com/BruceZhang1993/FastOCR", "repository": "https://github.com/BruceZhang1993/FastOCR"},
    author='Bruce Zhang',
    author_email='zttt183525594@gmail.com',
    license='LGPL-3.0-only',
    keywords='ocr',
    entry_points={"console_scripts": ["fastocr = fastocr.__main__:main"]},
    packages=['fastocr'],
    package_dir={"": "."},
    package_data={"fastocr": ["data/*.desktop", "data/*.ini", "data/*.pro", "i18n/*.qm", "i18n/*.ts", "qml/*.qml", "qml/component/*.qml", "resource/icon/dark/*.png", "resource/icon/dark/*.svg", "resource/icon/light/*.png", "resource/icon/light/*.svg"]},
    install_requires=['aiohttp', 'click', 'pyqt5', 'pyqt5-sip', 'qasync'],
    extras_require={"dev": ["dephell"], "linux": ["dbus-python"]},
)
